from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = "bloque/landing_page.html"
    extra_context = {
        "titulo_pagina" : "LANDING PAGE"
    }

class NosotrosPage(TemplateView):
    template_name = "bloque/nosotros.html"

class ContactoPage(TemplateView):
    template_name = "bloque/contacto.html"