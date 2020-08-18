from django.views.generic import TemplateView, DetailView, ListView
from django.core import serializers
from .models import Beach, BeachImage
# Create your views here.

class BeachListView(ListView):
    model = Beach
    template_name = 'beach_app/beach_list.html'
    context_object_name = 'beaches'

class BeachDetailView(DetailView):
    model = Beach
    template_name = 'beach_app/beach_detail.html'
    context_object_name = 'beach'

    def get_context_data(self, **kwargs):
        ctx = super(BeachDetailView, self).get_context_data(**kwargs)
        ctx['images'] = BeachImage.objects.filter(beach=self.get_object())
        return ctx

class BeachMapTemplateView(TemplateView):
    template_name = 'beach_app/beach_map.html'

    def get_context_data(self, **kwargs):
        ctx = super(BeachMapTemplateView, self).get_context_data(**kwargs)
        beaches = Beach.objects.all()
        ctx['beaches_json'] = serializers.serialize("geojson", beaches)
        return ctx
