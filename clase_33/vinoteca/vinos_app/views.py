from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import DeleteView , CreateView , UpdateView 
from .models import Vino

# Create your views here.
class VinosBaseView(View):
    template_name = 'pages/vinos.html'
    model = Vino
    fields = '__all__'
    success_url = reverse_lazy('vinos:all')

class VinosListView(VinosBaseView,ListView):
    """
    VISTAS
    """

class VinosDetailView(VinosBaseView, DetailView):
    """View to list the details from one vino.
    Use the 'vino' variable in the template to access
    the specific vino here and in the Views below"""

    template_name = "pages/vino_detail.html"

class VinosCreateView(VinosBaseView, CreateView):
    """View to create a new vino"""
    template_name = "pages/vino_crear.html"
    extra_context={
        "tipo":"Crear Vino"
    }
    success_url = reverse_lazy('vinos:all')


class VinosUpdateView(VinosBaseView, UpdateView):
    """View to update a vino"""
    template_name = "pages/vino_crear.html"
    extra_context={
        "tipo":"Actualizar Vino"
    }
    # los campos que quieran editar
    fields = ["nombre","rating"]


class VinosDeleteView(VinosBaseView, DeleteView):
    """View to delete a vino"""
    template_name = "pages/vino_delete.html"
    extra_context={
        "tipo":"Borrar Vino"
    }

