from rest_framework import serializers
from .models import ColorProduct, ImagesProduct, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ColorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorProduct
        fields = "__all__"


class ImagesProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = "__all__"