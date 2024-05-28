from rest_framework import serializers
from .models import Product, Service, ProductOption, ProductPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta: 
        models = ProductOption
        fields = '__all__'


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        models = ProductPrice
        fields = '__all__'

