from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

admin.site.site_header = "DrPhone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Core.urls')),
    # path('', include('BaseSettings.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)