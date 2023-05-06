from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('category/<str:category_name>/',
         views.category_products, name='category_products'),
    # 디테일
    path('<int:product_pk>/', views.product_detail, name='product_detail'),
    # 검색(쿼리스트링으로 받을꺼임)
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('add-to-cart/<int:product_id>/',
         views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:product_id>/',
         views.remove_from_cart, name='remove_from_cart'),
]
