from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Vino

# Create your views here.


class VinosBaseView(View):
    template_name = 'vinos.html'
    model = Vino
    fields = '__all__'
    success_url = reverse_lazy('vinos:all')
    

class VinosListView(VinosBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """
    
class VinosDetailView(VinosBaseView,DetailView):
    template_name = "vino_detail.html"
    
class VinosCreateView(VinosBaseView,CreateView):
    template_name = "vino_create.html"
    extra_context = {
        "tipo": "Crear vino"
    }
    
    
class VinosUpdateView(VinosBaseView,UpdateView):
    template_name = "vino_create.html"
    extra_context = {
        "tipo": "Actualizar vino"
    }
    
class VinosDeleteView(VinosBaseView,DeleteView):
    template_name = "vino_delete.html"
    extra_context = {
        "tipo": "Borrar vino"
    }
    