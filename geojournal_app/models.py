from django.contrib.gis.db import models
from django.urls import reverse

# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=225)
    location = models.PointField()
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('geojournal_app:list')

    def __str__(self):
        return self.name
