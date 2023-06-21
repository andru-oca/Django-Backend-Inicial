from django.shortcuts import render
from django.views.generic import TemplateView

# Function Based View
def VinotecaLanding(request):
    extra_context = {
        'base_on': 'Function Based View'
    } 
    return render(request, 'index.html', extra_context)



# Class Based View

class VinotecaLandingClassView(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'base_on': 'Class Based View'
    }