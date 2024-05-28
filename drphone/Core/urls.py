from django.urls import path
from .views import ProductAPIView, ServiceAPIView, ProductOptionAPIView, ProductPriceAPIView

urlsCoreApplication = [
    path('api/Core/productList', ProductAPIView.as_view()),
    path('api/Core/serviceList', ServiceAPIView.as_view()),
    path('api/Core/productOptionList', ProductOptionAPIView.as_view()),
    path('api/Core/productPriceList', ProductPriceAPIView.as_view())
]
