from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index')
    # path('category/<int:category_pk>/', views.category, name='category'),
    # path('category/<int:category_pk>/product/<int:product_pk>', views.product, name='product'),
]
