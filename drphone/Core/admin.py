from django.contrib import admin
from .models import NewDevices, ColorProduct, ImagesProduct

@admin.register(NewDevices)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ColorProduct)
class ColorProduct(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(ImagesProduct)
class ImagesProduct(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']