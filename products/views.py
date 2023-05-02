from django.shortcuts import render,redirect
from .models import Product, Category


# 백엔드에서 결과 확인하기 위하여 임시로 import
from django.http import JsonResponse
from django.forms.models import model_to_dict


def init(request):
    return redirect('products:index')

# 임시 인덱스(나중에는 좋아요 많은순 or 리뷰 많은 순으로 상품 대체할듯?)
def index(request):
    # 모든 제품
    products = Product.objects.order_by('-pk')[0:16]
    context = {
        'products':products,
    }

    return render(request, 'products/index.html', context)


# 카테고리별 상품
def category_products(request, category_name):
    # 특정 카테고리의 상품들
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    

    context = {
        'category':category_name,
        'products':products,
    }
    
    return render(request, 'products/category.html', context)


# 상품 디테일
def product_detail(request, product_pk):
    # 특정상품 조회
    product = Product.objects.get(pk=product_pk)

    # 임시
    product_dict = model_to_dict(product)
    product_dict['image'] = product.image.url

    context = {
        'product':product_dict,
    }
    
    # 임시 json 리스폰스 - 나중에 html로 렌더링
    return JsonResponse(context, status=200)
    # return render(request, 'products/index.html', context)