from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import UserModel, ProductModel, CategoryModel, OrderModel, HistoryOrderModel
from .serilizers import UserSerializer, ProductModelSerializer, CategorySerializer, ProductDetailsSerializer, \
    OrderModelSerializer, HistoryModelSerializer


# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch']


class CategoryViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class ProductModelViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    http_method_names = ['get']


class ProductDetailsViewSet(generics.RetrieveUpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductDetailsSerializer


class OrderViewSet(generics.CreateAPIView, generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelSerializer


class HistoryViewSet(ModelViewSet):
    queryset = HistoryOrderModel.objects.all()
    serializer_class = HistoryModelSerializer
