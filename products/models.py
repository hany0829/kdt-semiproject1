from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

class Product(models.Model):
    def product_image_path(instance, filename):
        png = filename.split('.')[-1]
        return f'images/{instance.category.name.lower()}/{instance.name}.{png}'
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name     = models.CharField(max_length=50)
    price    = models.PositiveIntegerField()
    origin   = models.CharField(max_length=50, default='JAPAN')
    brand    = models.CharField(max_length=50, default='Karimoku')
    image    = models.ImageField(upload_to=product_image_path)
