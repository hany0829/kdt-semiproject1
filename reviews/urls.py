from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('category/<int:category_pk>/product/<int:product_pk>/review/create/', views.create_review, name='create_review'),
    path('category/<int:category_pk>/product/<int:product_pk>/review/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('category/<int:category_pk>/product/<int:product_pk>/review/<int:review_pk>/delete/', views.delete_review, name='delete_review'),
    path('category/<int:category_pk>/product/<int:product_pk>/review/<int:review_pk>/update/', views.delete_review, name='delete_review'),

    # path('<int:review_pk>/like/', views.category, name='category'),

    # path('<int:review_pk>/comments/', views.comments, name='comments'),
    # path('<int:review_pk>/comments/<int:comment_pk>', views.comments_like, name='comments_like'),
    # path('<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    # path('<int:review_pk>/comments/<int:comment_pk>/update/', views.comments_update, name='comments_update'),
]
