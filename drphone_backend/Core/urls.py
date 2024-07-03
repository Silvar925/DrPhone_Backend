from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PhonesAPIView, PhonesOptionsAPIView, AccessoriesAPIView, CoversAPIView, IMacAPIView, \
    IMacOptionsAPIView, AccessoriesOptionsAPIView

router = DefaultRouter()

# Регистрация представлений в роутере
router.register(r'phones', PhonesAPIView, basename='phones')
router.register(r'phones-options', PhonesOptionsAPIView, basename='phones-options')
router.register(r'accessories', AccessoriesAPIView, basename='accessories')
router.register(r'accessories-options', AccessoriesOptionsAPIView, basename='accessories-options')
router.register(r'covers', CoversAPIView, basename='covers')
router.register(r'imac', IMacAPIView, basename='imac')
router.register(r'imac-options', IMacOptionsAPIView, basename='imac-options')

urlpatterns = [
    path('api/Core/', include(router.urls)),
]