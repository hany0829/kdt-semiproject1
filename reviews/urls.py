from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('product/<int:product_pk>/review/create/', views.create_review, name='create_review'),
    path('product/<int:product_pk>/review/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
    path('product/<int:product_pk>/review/<int:review_pk>/update/', views.update_review, name='update_review'),

    path('product/<int:product_pk>/review/<int:review_pk>/comment/create/', views.comment_create, name='comment_create'),
    path('product/<int:product_pk>/review/<int:review_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),

    path('product/<int:product_pk>/review/<int:review_pk>/likes/', views.like_review, name='like_review'),
    path('product/<int:product_pk>/review/<int:review_pk>/comment/<int:comment_pk>/like/', views.like_comment, name='like_comment')
]
