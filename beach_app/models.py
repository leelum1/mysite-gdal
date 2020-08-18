from django.contrib.gis.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from markdownx.models import MarkdownxField

class Beach(models.Model):
    TYPES = (
        ('Beach', 'Beach'),
        ('Mountain', 'Mountain'),
        ('Cave', 'Cave'),
        ('Waterfall', 'Waterfall'),
        ('River', 'River'),
        ('Birdwatching', 'Birdwatching'),
    )

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()

    has_parking = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='beach_images/', blank=True, null=True)
    description = MarkdownxField(null=True)
    location = models.PointField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('beach_app:detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class BeachImage(models.Model):
    beach = models.ForeignKey(Beach, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='beach_images/')
    caption = models.TextField(null=True, blank=True)
    photographer = models.CharField(max_length=255, null=True, blank=True)
    date_captured = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.hike.name

def create_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(create_slug, sender=Beach)
