from django.contrib.gis import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['name', 'location', 'description',]
        labels = {
            'name': 'Name',
            'location': 'Location',
            'description': 'Description'
        }
        widgets = {
            'location': forms.OSMWidget(
                attrs={
                    'map_width': 800,
                    'map_height': 500,
                    'default_zoom':3,
                }
            )
        }
