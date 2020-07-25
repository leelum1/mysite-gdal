from django.views.generic import TemplateView, DetailView, ListView
from django.core import serializers
from .models import Hike, HikeImage
# Create your views here.

class HikeSafetyTemplateView(TemplateView):
    template_name = 'hike_app/hike_safety.html'

class HikeListView(ListView):
    model = Hike
    template_name = 'hike_app/hike_list.html'
    context_object_name = 'hikes'
    # paginate_by = 10

class HikeDetailView(DetailView):
    model = Hike
    template_name = 'hike_app/hike_detail.html'
    context_object_name = 'hike'

    def get_context_data(self, **kwargs):
        ctx = super(HikeDetailView, self).get_context_data(**kwargs)
        ctx['images'] = HikeImage.objects.filter(hike=self.get_object())
        ctx['similar_hikes'] = Hike.objects.filter(region=self.get_object().region).exclude(id=self.get_object().id)[:3]
        return ctx

class HikeMapTemplateView(TemplateView):
    template_name = 'hike_app/hike_map.html'

    def get_context_data(self, **kwargs):
        ctx = super(HikeMapTemplateView, self).get_context_data(**kwargs)
        hikes = Hike.objects.all()
        ctx['hikes_json'] = serializers.serialize("geojson", hikes)
        return ctx
