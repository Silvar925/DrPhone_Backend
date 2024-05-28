from rest_framework import generics
from .models import ColorProduct, ImagesProduct, NewDevices
from .serializer import ColorProductSerializer, ImagesProductSerializer, ProductSerializer


class ProductAPIView(generics.ListAPIView):
    queryset = NewDevices.objects.all()
    serializer_class = ProductSerializer


class ColorProductAPIView(generics.ListAPIView):
    queryset = ColorProduct.objects.all()
    serializer_class = ColorProductSerializer


class ImagesProductAPIView(generics.ListAPIView):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductSerializer