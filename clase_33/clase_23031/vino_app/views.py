from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Vino


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView , DeleteView



# Create your views here.

class VinoBaseView():
    template_name = "vinos.html"
    model = Vino
    fields =  "__all__"
    success_url = reverse_lazy("vinos:all")

class VinoListView(VinoBaseView,ListView):
    """
    Muestra todos los vinos
    """
    
    
class VinoDetailView(VinoBaseView,DetailView):
    template_name = "vinos_detail.html"

    
    
class VinoCreateView(VinoBaseView,CreateView):
    template_name = "vinos_create.html"
    extra_context = {
        "tipo" : "Crear vinito"
    }
    
class VinoUpdateView(VinoBaseView,UpdateView):
    template_name = "vinos_create.html"
    extra_context = {
        "tipo" : "Actualiza vinito"
    }

class VinoDeleteView(VinoBaseView,DeleteView):
    template_name = "vinos_delete.html"
    extra_context = {
        "tipo" : "Borrar vinito"
    }
