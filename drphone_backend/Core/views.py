from django.shortcuts import render
from rest_framework import generics
from .models import Phones, PhonesOptions, Accessories, Covers, IMac, IMacOptions, AccessoriesOptions
from .serializer import PhonesSerializer, PhonesOptionsSerializer, AccessoriesSerializer, CoversSerializer, IMacSerializer, IMacOptionsSerializer, AccessoriesOptionsSerializer


class PhonesAPIView(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesOptionsAPIView(generics.ListAPIView):
    queryset = PhonesOptions.objects.all()
    serializer_class = PhonesOptionsSerializer


class AccessoriesAPIView(generics.ListAPIView):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer

class AccessoriesOptionsAPIView(generics.ListAPIView):
    queryset = AccessoriesOptions.objects.all()
    serializer_class = AccessoriesOptionsSerializer


class CoversAPIView(generics.ListAPIView):
    queryset = Covers.objects.all()
    serializer_class = CoversSerializer


class IMacAPIView(generics.ListAPIView):
    queryset = IMac.objects.all()
    serializer_class = IMacSerializer


class IMacOptionsAPIView(generics.ListAPIView):
    queryset = IMacOptions.objects.all()
    serializer_class = IMacOptionsSerializer