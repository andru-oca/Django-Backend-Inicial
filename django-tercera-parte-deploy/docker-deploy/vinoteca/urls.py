from django.contrib import admin
from django.urls import path , include

from .views import Vinoteca

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Vinoteca.as_view(), name="vinoteca"),
    path("vinos/", include("vino_app.urls")),
]
