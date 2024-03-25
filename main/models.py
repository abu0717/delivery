from django.db import models
from django.contrib.auth.models import AbstractUser
from .validator import validate_phone_number
from django.core.exceptions import ValidationError


# Create your models here.

class UserModel(models.Model):
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13, validators=[validate_phone_number], unique=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class ProductModel(models.Model):
    img = models.ImageField(upload_to='media/products')
    product_name = models.CharField(max_length=200)
    product_price = models.PositiveIntegerField()
    product_description = models.TextField()
    quantity = models.PositiveIntegerField(null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def clean(self):
        if self.product_price <= 100:
            raise ValidationError('product price can not be less than 100')

    def __str__(self):
        return self.product_name


class OrderModel(models.Model):
    product = models.ManyToManyField(ProductModel)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HistoryOrderModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(ProductModel)

    is_accepted = models.BooleanField(default=False)
    is_cooking = models.BooleanField(default=False)
    is_courier = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
