from django.contrib import admin
from .models import ColorProduct, ImagesProduct, MemoryProducts, SIMProduct, Manufacturer, RAM


@admin.register(ColorProduct)
class ColorProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'codeColor']
    search_fields = ['name', 'codeColor']


@admin.register(ImagesProduct)
class ImagesProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name', 'image']


@admin.register(MemoryProducts)
class MemoryProductsAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']


@admin.register(SIMProduct)
class SIMProductAdmin(admin.ModelAdmin):
    list_display = ['type']
    search_fields = ['type']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ['size']
    search_fields = ['size']