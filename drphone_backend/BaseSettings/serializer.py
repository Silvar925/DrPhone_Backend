from rest_framework import serializers
from .models import ColorProduct, ImagesProduct, MemoryProducts, SIMProduct, Manufacturer, RAM


class ColorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorProduct
        fields = '__all__'


class ImagesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = '__all__'


class MemoryProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryProducts
        fields = '__all__'


class SIMProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SIMProduct
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'