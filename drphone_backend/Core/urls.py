from django.urls import path
from .views import PhonesAPIView, PhonesOptionsAPIView, AccessoriesAPIView, CoversAPIView, IMacAPIView, IMacOptionsAPIView, AccessoriesOptionsAPIView

urlPatternsCore = [
    path('api/Core/PhonesAPIView', PhonesAPIView.as_view()),
    path('api/Core/PhonesOptionsAPIView', PhonesOptionsAPIView.as_view()),
    path('api/Core/AccessoriesAPIView', AccessoriesAPIView.as_view()),
    path('api/Core/AccessoriesOptionsAPIView', AccessoriesOptionsAPIView.as_view()),
    path('api/Core/CoversAPIView', CoversAPIView.as_view()),
    path('api/Core/IMacAPIView', IMacAPIView.as_view()),
    path('api/Core/IMacOptionsAPIView', IMacOptionsAPIView.as_view()),
]
