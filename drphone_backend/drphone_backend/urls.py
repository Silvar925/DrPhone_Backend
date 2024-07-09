from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from BaseSettings.urls import urlPatternsBaseSettings

admin.site.site_header = "DrPhone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    path('', include(urlPatternsBaseSettings))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)