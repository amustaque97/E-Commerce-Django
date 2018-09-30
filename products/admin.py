from django.contrib import admin
from .models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug': ('product_title',)}

admin.site.register(Products, ProductsAdmin)
