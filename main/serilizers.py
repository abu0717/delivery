from phonenumbers.unicode_util import Category
from rest_framework import serializers
from .models import UserModel, CategoryModel, ProductModel, OrderModel, HistoryOrderModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    confirm_password = serializers.CharField(max_length=200, write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password do not match")
        elif len(attrs['password']) < 6:
            raise serializers.ValidationError("Password length is too short, it must be at least 8 characters")
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('confirm_password')
        return super().update(instance, validated_data)


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['product_description', 'category']


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        exclude = ['category']


class CategorySerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        exclude = ['created_at', 'updated_at']

    def get_product(self, obj):
        product = ProductModel.objects.filter(category_id=obj.id)
        serializer = ProductModelSerializer(instance=product, many=True)
        return serializer.data


class OrderModelSerializer(serializers.ModelSerializer):
    # product = serializers.SerializerMethodField()

    class Meta:
        model = OrderModel
        fields = '__all__'

    # def get_product(self, obj):
    #     product = ProductModel.objects.filter(product_id=obj.id)
    #     serializer = ProductModelSerializer(instance=product, many=True)
    #     return serializer.data


class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryOrderModel
        fields = '__all__'