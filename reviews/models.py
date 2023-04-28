from django.db import models
from django.conf import settings

# from products.models import Product

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

# class Comment(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     content = models.CharField(max_length=200)
#     created
