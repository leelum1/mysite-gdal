from django.views.generic import TemplateView
# Create your views here.

class WatershedMapTemplateView(TemplateView):
    template_name = 'watershed_app/watershed_map.html'
