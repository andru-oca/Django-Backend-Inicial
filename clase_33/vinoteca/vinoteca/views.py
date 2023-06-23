from django.shortcuts import render
from django.views.generic import TemplateView


class VinotecaLandingClassView(TemplateView):
    template_name = 'pages/index.html'
    extra_context = {
        'base_on': 'Class Based View'
    }