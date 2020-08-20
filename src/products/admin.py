from django.contrib import admin

from .models import product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description']

admin.site.register(product, ProductAdmin)