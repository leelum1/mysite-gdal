from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core import serializers
from .models import Entry
from .forms import EntryForm
# Create your views here.

class GeojournalTemplateView(TemplateView):
    template_name = 'geojournal_app/geojournal.html'

class EntryListView(ListView):
    model = Entry
    template_name = 'geojournal_app/entry_list.html'
    context_object_name = 'entries'

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'geojournal_app/entry_form.html'

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'geojournal_app/entry_form.html'

class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'geojournal_app/entry_delete.html'
    success_url = reverse_lazy('blog_app:list')
