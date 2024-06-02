from django.contrib import admin
from django.urls import path, include
from Core.urls import urlPatternsCore
from BaseSettings.urls import urlPatternsBaseSettings

admin.site.site_header = "DrPhone"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlPatternsCore)),
    path('', include(urlPatternsBaseSettings))
]
