from django.views.generic import TemplateView
from django.shortcuts import render


class IndexPage(TemplateView):
    template_name = "index.html"
