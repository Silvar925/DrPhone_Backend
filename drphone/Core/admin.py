from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import NewDevices, ColorProduct, ImagesProduct, UsedDevices, Accessories, Covers, IMac


@admin.register(NewDevices)
class NewDevicesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ColorProduct)
class ColorProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ImagesProduct)
class ImagesProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(UsedDevices)
class UsedDevicesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Covers)
class CoversAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(IMac)
class IMacAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']