from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    enabled = models.BooleanField(default=True)
    description = models.TextField()
    discount = models.FloatField(default=0)
    image = models.ImageField(upload_to='covers/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='products')


class Category(models.Model):
    name = models.CharField(max_length=255)
