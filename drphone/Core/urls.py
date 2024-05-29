from django.urls import path
from .views import NewDevicesAPIView, ColorProductAPIView, ImagesProductAPIView, UsedDevicesAPIView, AccessoriesAPIView, CoversAPIView, IMacAPIView

urlpatternsCore = [
    path('api/v1/NewDevicesAPIView', NewDevicesAPIView.as_view()),
    path('api/v1/UsedDevicesAPIView', UsedDevicesAPIView.as_view()),
    path('api/v1/AccessoriesAPIView', AccessoriesAPIView.as_view()),
    path('api/v1/CoversAPIView', CoversAPIView.as_view()),
    path('api/v1/IMacAPIView', IMacAPIView.as_view()),
    path('api/v1/ColorProductAPIView', ColorProductAPIView.as_view()),
    path('api/v1/ImagesProductAPIView', ImagesProductAPIView.as_view())
]
