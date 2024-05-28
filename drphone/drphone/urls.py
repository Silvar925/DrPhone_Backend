from django.contrib import admin
from django.urls import path, include
from Core.urls import urlpatternsCore

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(urlpatternsCore))
]
