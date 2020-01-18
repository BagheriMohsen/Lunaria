from django.contrib import admin

# Register your models here.
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display    =   ['title','created_at','updated_at']
    list_filter     =   ['created_at','updated_at']
    search_fields   =   ['title',]