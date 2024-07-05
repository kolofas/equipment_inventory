from django.contrib import admin
from .models import Stock, Category, Equipment


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['location']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_filter = ['category', 'stock', 'user']
