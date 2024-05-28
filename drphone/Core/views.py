from rest_framework import generics
from .serializer import ProductSerializer, ServiceSerializer, ProductOptionSerializer, ProductPriceSerializer
from .models import Product, Service, ProductOption, ProductPrice


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ServiceAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ProductOptionAPIView(generics.ListAPIView):
    queryset = ProductOption.objects.all()
    serializer_class = ProductOptionSerializer


class ProductPriceAPIView(generics.ListAPIView):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer