from django.views.generic import TemplateView


class Landing(TemplateView):
    template_name = "page/landing_page.html"

class Contacto(TemplateView):
    template_name = "page/contacto.html"

class QuienesSomos(TemplateView):
    template_name = "page/quienesSomos.html"
    
class Sales(TemplateView):
    template_name = "page/sales.html"
