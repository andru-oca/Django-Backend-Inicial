from django.contrib import admin
from .models import Vino

# Register your models here.

@admin.register(Vino)
class VinoAdmin(admin.ModelAdmin):
    ...