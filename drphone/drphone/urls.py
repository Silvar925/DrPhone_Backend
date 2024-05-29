from django.contrib import admin
from django.urls import path, include
from Core.urls import urlpatternsCore


admin.site.site_header = "Dr.Phone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(urlpatternsCore))
]
