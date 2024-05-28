from django.contrib import admin
from .models import Product, ColorProduct, ImagesProduct

@admin.register(Product)
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