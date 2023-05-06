from django.db import models
import os


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    def product_image_path(instance, filename):
        _, ext = os.path.splitext(filename)
        return f'images/{instance.category.name.lower()}/{instance.name}{ext}'
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    origin = models.CharField(max_length=50, default='JAPAN')
    brand = models.CharField(max_length=50, default='Karimoku')
    image = models.ImageField(upload_to=product_image_path)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # 이미지 파일을 삭제합니다.
        self.image.delete()
        super().delete(*args, **kwargs)
