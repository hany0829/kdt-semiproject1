from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    # 카테고리 별로 상품 나오는
    # path('category/<str:category_name>/page/<int:page>/',
    #      views.category_products, name='category_products'),
    path('category/<str:category_name>/',
         views.category_products, name='category_products'),
    # 디테일
    path('<int:product_pk>/', views.product_detail, name='product_detail'),
    # 검색(쿼리스트링으로 받을꺼임)
    path('search/', views.search, name='search'),
    # 인덱스
    path('', views.index, name='index'),
]
