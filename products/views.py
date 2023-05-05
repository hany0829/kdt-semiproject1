from django.shortcuts import render, redirect
from .models import Product, Category
# 리뷰관련
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Count


def init(request):
    return redirect('products:index')

# 임시 인덱스(나중에는 좋아요 많은순 or 리뷰 많은 순으로 상품 대체할듯?)


def index(request):
    # 베스트 프로덕트(리뷰순)
    products = Product.objects.annotate(
        review_count=Count("reviews")).order_by("-review_count")
    print(products)
    context = {
        'products': products,
    }

    return render(request, 'products/index.html', context)


# 카테고리별 상품
def category_products(request, category_name):
    # 특정 카테고리의 상품들
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    order_param = request.GET.get('order', None)  # 파라미터 받아오기

    # 정렬하기
    if order_param == 'latest':  # 최신순
        products = products.order_by('-pk')
    elif order_param == 'low_price':  # 낮은 가격순
        products = products.order_by('price')
    elif order_param == 'high_price':  # 높은 가격순
        products = products.order_by('-price')
    elif order_param == 'many_reviews':  # 리뷰 많은 순
        products = Product.objects.annotate(
            review_count=Count("reviews")).order_by("-review_count")

    context = {
        'category': category_name,
        'products': products,
    }

    return render(request, 'products/category.html', context)


# 상품 디테일
def product_detail(request, product_pk):
    # 특정상품 조회
    product = Product.objects.get(pk=product_pk)
    form = ReviewForm()
    reviews = Review.objects.filter(product=product)
    # comments = reviews.comment_set.all()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
        # 'comments':comments,
    }

    return render(request, 'products/detail.html', context)


# 상품 검색
def search(request):
    query = request.GET.get('searched', '')
    products = Product.objects.filter(name__contains=query)

    context = {
        'products': products,
    }

    return render(request, 'products/search.html', context)
