from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import View
from .models import Vino


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView


# Create your views here.


class VinoBaseView(View):
    template_name = "vino.html"
    model = Vino
    fields = "__all__"
    success_url = reverse_lazy("vinos:all")
    

class VinoListView(VinoBaseView,ListView):
    ...

class VinoDetailView(VinoBaseView,DetailView):
    template_name = "vino_detail.html"
    

class VinoCreateView(VinoBaseView,CreateView):
    template_name = "vino_create.html"
    extra_context = {
        "tipo" : "crear vino"
    }

class VinoUpdateView(VinoBaseView,UpdateView):
    template_name = "vino_create.html"
    extra_context = {
        "tipo" : "actualizar vino"
    }

class VinoDeleteView(VinoBaseView,DeleteView):
    template_name = "vino_delete.html"
    extra_context = {
        "tipo" : "borrar vino"
    }