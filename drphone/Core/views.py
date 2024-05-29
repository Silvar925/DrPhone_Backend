from rest_framework import generics
from .models import ColorProduct, ImagesProduct, NewDevices, UsedDevices, Accessories, Covers, IMac
from .serializer import ColorProductSerializer, ImagesProductSerializer, NewDevicesSerializer, UsedDevicesSerializer, AccessoriesSerializer, CoversSerializer, IMac


class NewDevicesAPIView(generics.ListAPIView):
    queryset = NewDevices.objects.all()
    serializer_class = NewDevicesSerializer


class UsedDevicesAPIView(generics.ListAPIView):
    queryset = UsedDevices.objects.all()
    serializer_class = UsedDevicesSerializer


class AccessoriesAPIView(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class CoversAPIView(generics.ListAPIView):
    queryset = Covers.objects.all()
    serializer_class = CoversSerializer


class IMacAPIView(generics.ListAPIView):
    queryset = IMac.objects.all()
    serializer_class = IMac    


class ColorProductAPIView(generics.ListAPIView):
    queryset = ColorProduct.objects.all()
    serializer_class = ColorProductSerializer


class ImagesProductAPIView(generics.ListAPIView):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductSerializer