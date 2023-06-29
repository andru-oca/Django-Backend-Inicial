from django.views.generic import TemplateView

class Vinoteca(TemplateView):
    template_name = "index.html"
    