from django.contrib import admin
from django.urls import path
from .router import router

urlpatterns = router.urls