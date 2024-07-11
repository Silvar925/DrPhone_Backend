from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Phones, PhonesOptions, Accessories, Covers, IMac, IMacOptions, AccessoriesOptions
from .serializer import PhonesSerializer, PhonesOptionsSerializer, AccessoriesSerializer, CoversSerializer, \
    IMacSerializer, IMacOptionsSerializer, AccessoriesOptionsSerializer, PhoneOptionsListSerializer


class PhonesAPIView(viewsets.ModelViewSet):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer


class PhonesOptionsAPIView(viewsets.ModelViewSet):
    queryset = PhonesOptions.objects.all()
    serializer_class = PhonesOptionsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['unique_id']


class PhoneOptionsListAPIView(viewsets.ModelViewSet):
    queryset = PhonesOptions.objects.all()
    serializer_class = PhoneOptionsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['unique_id']


class AccessoriesAPIView(viewsets.ModelViewSet):
    queryset = Accessories.objects.all()
    serializer_class = AccessoriesSerializer


class AccessoriesOptionsAPIView(viewsets.ModelViewSet):
    queryset = AccessoriesOptions.objects.all()
    serializer_class = AccessoriesOptionsSerializer


class CoversAPIView(viewsets.ModelViewSet):
    queryset = Covers.objects.all()
    serializer_class = CoversSerializer


class IMacAPIView(viewsets.ModelViewSet):
    queryset = IMac.objects.all()
    serializer_class = IMacSerializer


class IMacOptionsAPIView(viewsets.ModelViewSet):
    queryset = IMacOptions.objects.all()
    serializer_class = IMacOptionsSerializer
