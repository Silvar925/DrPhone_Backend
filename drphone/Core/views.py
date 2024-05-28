from rest_framework import generics
from .models import ColorProduct, ImagesProduct, Product
from .serializer import ColorProductSerializer, ImagesProductSerializer, ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorProductAPIView(generics.ListAPIView):
    queryset = ColorProduct.objects.all()
    serializer_class = ColorProductSerializer


class ImagesProductAPIView(generics.ListAPIView):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductSerializer