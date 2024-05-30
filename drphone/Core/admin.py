from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import AdminSite
from .models import NewDevices, ColorProduct, ImagesProduct, UsedDevices, Accessories, Covers, IMac


@admin.register(NewDevices)
class NewDevicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_color', 'color', 'memory', 'price']
    search_fields = ['name', 'price', 'color__name', 'color', 'memory']
    filter_horizontal = ['allColors', 'images']
    list_filter = ['color__name', 'memory', 'price']

    def display_color(self, obj):
        return ', '.join([color.name for color in obj.allColors.all()])

    display_color.short_description = 'Все варианты цветов'


@admin.register(ColorProduct)
class ColorProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'codeColor']
    search_fields = ['name', 'codeColor']


@admin.register(ImagesProduct)
class ImagesProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo']
    search_fields = ['name', 'photo']


@admin.register(UsedDevices)
class UsedDevicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_color', 'memory', 'price']
    search_fields = ['name', 'price', 'color__name', 'memory']
    filter_horizontal = ['color', 'images']
    list_filter = ['color__name', 'memory', 'price']

    def display_color(self, obj):
        return ', '.join([color.name for color in obj.color.all()])

    display_color.short_description = 'Цвет товара'



@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']


@admin.register(Covers)
class CoversAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']


@admin.register(IMac)
class IMacAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']