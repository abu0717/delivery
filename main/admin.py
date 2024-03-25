from django.contrib import admin
from .models import UserModel, CategoryModel, ProductModel, OrderModel, HistoryOrderModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(CategoryModel)
admin.site.register(ProductModel)
admin.site.register(OrderModel)
admin.site.register(HistoryOrderModel)