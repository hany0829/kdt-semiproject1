from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # 카테고리 별로 상품 나오는
    path('category/<str:category_name>/', views.category_products, name='category_products'),
    # 상품 디테일
    # path('category/<int:category_pk>/product/<int:product_pk>', views.category_products, name='category_products'),
    path('<int:product_pk>/', views.product_detail, name='product_detail'),
    path('', views.index, name='index')
]
