from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from Core.urls import urlpatternsCore


admin.site.site_header = "Dr.Phone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(urlpatternsCore))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)