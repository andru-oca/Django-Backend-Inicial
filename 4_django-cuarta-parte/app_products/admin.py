from django.contrib import admin
from .models import Product , Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    ...
