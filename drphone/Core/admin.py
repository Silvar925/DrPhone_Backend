from django.contrib import admin
from .models import Product, Service, ProductOption, ProductPrice, ProductImage


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']


@admin.register(ProductOption)
class ProductOption(admin.ModelAdmin):
    list_display = ['product', 'color', 'memory', 'sim_type']
    search_fields = ['product', 'color', 'memory', 'sim_type']


@admin.register(ProductPrice)
class ProductPrice(admin.ModelAdmin):
    list_display = ['product_option', 'price']
    search_fields = ['product_option', 'price']


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
    search_fields = ['id']  # Добавьте поля, по которым вы хотите выполнять поиск