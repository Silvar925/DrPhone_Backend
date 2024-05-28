from django.urls import path
from .views import ProductAPIView, ColorProductAPIView, ImagesProductAPIView

urlpatternsCore = [
    path('api/v1/ProductAPIView', ProductAPIView.as_view()),
    path('api/v1/ColorProductAPIView', ColorProductAPIView.as_view()),
    path('api/v1/ImagesProductAPIView', ImagesProductAPIView.as_view())
]
