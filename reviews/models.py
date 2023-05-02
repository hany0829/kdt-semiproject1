from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    # 리뷰 좋아요
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    # 이미지
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # 별점 구현
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)