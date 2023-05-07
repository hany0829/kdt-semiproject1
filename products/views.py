from django.shortcuts import render, redirect
from .models import Product, Category
# 리뷰관련
from reviews.models import Review
from reviews.forms import ReviewForm
from django.db.models import Count
from django.core.paginator import Paginator
from decimal import Decimal


def init(request):
    return redirect('products:index')


def index(request):
    # 베스트 프로덕트(리뷰순)
    products = Product.objects.annotate(
        review_count=Count("reviews")).order_by("-review_count")[0:8]

    context = {
        'products': products,
    }

    return render(request, 'products/index.html', context)


# 카테고리별 상품
def category_products(request, category_name):
    category = Category.objects.get(name=category_name)
    products = Product.objects.select_related('category').filter(category=category).order_by('-pk')
    products_num = products.count()
    # 페이지
    page = request.GET.get('page', '1')

    # 파라미터 받아오기
    order_param = request.GET.get('order', 'latest')

    # 정렬하기
    if order_param == 'latest':  # 최신순
        products = products.order_by('-pk')
    elif order_param == 'low_price':  # 낮은 가격순
        products = products.order_by('price')

    elif order_param == 'high_price':  # 높은 가격순
        products = products.order_by('-price')

    elif order_param == 'many_reviews':  # 리뷰 많은 순
        products = Product.objects.prefetch_related('reviews').annotate(
            review_count=Count("reviews")).order_by("-review_count")

    paginator = Paginator(products, 16)  # 페이지당 16개씩 보여주기
    products = paginator.get_page(page)

    context = {
        'category': category_name,
        'products': products,
        'order_param': order_param,
        'products_num': products_num,
    }

    return render(request, 'products/category.html', context)


# 상품 디테일
def product_detail(request, product_pk):
    # 특정상품 조회
    product = Product.objects.get(pk=product_pk)
    form = ReviewForm()
    reviews = Review.objects.select_related('user').prefetch_related(
                                            'comment_set',
                                            'comment_set__user',
                                            'comment_set__like_users'
                                            ).filter(product=product)
    

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
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


# 장바구니
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'quantity': quantity, 'price': str(product.price)}

    request.session['cart'] = cart

    return redirect('products:view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0

    for product_id, product_info in cart.items():
        product = Product.objects.get(id=product_id)
        total_price = Decimal(product_info['quantity']) * product.price
        cart_total += total_price
        cart_items.append({
            'product': product,
            'quantity': product_info['quantity'],
            'total_price': total_price,
        })

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'products/cart.html', context)


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return redirect('products:view_cart')
