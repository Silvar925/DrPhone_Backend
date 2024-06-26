from django.contrib import admin
from .models import PhonesOptions, Phones, Accessories, AccessoriesOptions, Covers, IMac, IMacOptions
from transliterate import translit, get_available_language_codes


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'display_color', 'display_memory']
    search_fields = ['name', 'manufacturer', 'display_color', 'display_memory']

    list_filter = ['manufacturer', 'allColors', 'allMemory', 'allSim']
    
    def display_color(self, obj):
        return ', '.join([color.name for color in obj.allColors.all()])

    display_color.short_description = 'Все варианты цветов'


    def display_memory(self, obj):
        return ', '.join([memory.size for memory in obj.allMemory.all()])

    display_memory.short_description = 'Все объемы памяти'


@admin.register(PhonesOptions)
class PhonesOptionsAdmin(admin.ModelAdmin):
    list_display = ['phone', 'color', 'memory', 'sim']
    search_fields = ['name', 'manufacturer', 'allColors__name', 'allMemory__size']

    list_filter = ['phone', 'color', 'memory', 'sim']


@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']


@admin.register(Covers)
class CoversAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']


@admin.register(AccessoriesOptions)
class AccessoriesOptionsAdmin(admin.ModelAdmin):
    list_display = ['accessories', 'color', 'memory', 'sim']
    search_fields = ['accessories', 'color', 'memory', 'sim']


@admin.register(IMac)
class IMacAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(IMacOptions)
class IMacOptionsSerializer(admin.ModelAdmin):
    list_display = ['imac', 'color', 'memory', 'price']
    search_fields = ['imac', 'color', 'memory', 'price']