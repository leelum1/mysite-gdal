from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
class SteelbandsTemplateView(TemplateView):
    template_name = 'steelbands_app/steelbands.html'
