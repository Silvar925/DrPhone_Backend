from django.shortcuts import render
from rest_framework import generics
from .models import ColorProduct, ImagesProduct, MemoryProducts, SIMProduct, Manufacturer
from .serializer import ColorProductSerializer, ImagesProductSerializer, MemoryProductsSerializer, SIMProductSerializer, ManufacturerSerializer


class ColorProductAPIView(generics.ListAPIView):
    queryset = ColorProduct.objects.all()
    serializer_class = ColorProductSerializer


class ImagesProductAPIView(generics.ListAPIView):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductSerializer


class MemoryProductsAPIView(generics.ListAPIView):
    queryset = MemoryProducts.objects.all()
    serializer_class = MemoryProductsSerializer


class SIMProductAPIView(generics.ListAPIView):
    queryset = SIMProduct.objects.all()
    serializer_class = SIMProductSerializer


class ManufacturerAPIView(generics.ListAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer