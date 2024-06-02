from django.urls import path
from .views import ColorProductAPIView, ImagesProductAPIView, MemoryProductsAPIView, SIMProductAPIView, ManufacturerAPIView


urlPatternsBaseSettings = [
    path('api/BaseSettings/ColorProductAPIView', ColorProductAPIView.as_view()),
    path('api/BaseSettings/ImagesProductAPIView', ImagesProductAPIView.as_view()),
    path('api/BaseSettings/MemoryProductsAPIView', MemoryProductsAPIView.as_view()),
    path('api/BaseSettings/SIMProductAPIView', SIMProductAPIView.as_view()),
    path('api/BaseSettings/ManufacturerAPIView', ManufacturerAPIView.as_view()),
]
