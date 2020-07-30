from django.contrib.gis.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from markdownx.models import MarkdownxField

class Hike(models.Model):
    DIFFICULTY = (
        ('1', 'Very Easy'),
        ('2', 'Easy'),
        ('3', 'Basic Fitness Required'),
        ('4', 'Strenuous'),
        ('5', 'Very Difficult'),
    )

    TYPES = (
        ('Beach', 'Beach'),
        ('Mountain', 'Mountain'),
        ('Cave', 'Cave'),
        ('Waterfall', 'Waterfall'),
        ('River', 'River'),
        ('Birdwatching', 'Birdwatching'),
    )

    REGIONS = (
        ('northwest', 'NorthWest'),
        ('northeast', 'NorthEast'),
        ('central', 'Central'),
        ('south', 'South'),
        ('windward', 'Windward'),
        ('leeward', 'Leeward'),
    )

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField()
    type = models.CharField(max_length=125, choices=TYPES, default='Waterfall')
    difficulty = models.CharField(max_length=125, choices=DIFFICULTY)
    region = models.CharField(max_length=125, choices=REGIONS)
    time = models.CharField(max_length=125, blank=True, null=True)
    has_parking = models.BooleanField(default=False)
    kid_friendly = models.BooleanField(default=False)
    swimming_required = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='hike_images/', blank=True, null=True)
    description = MarkdownxField(null=True)
    trailhead_point = models.PointField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('hike_app:detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class HikeImage(models.Model):
    hike = models.ForeignKey(Hike, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='hike_images/')
    caption = models.TextField(null=True, blank=True)
    photographer = models.CharField(max_length=255, null=True, blank=True)
    date_captured = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.hike.name

def create_slug(sender, instance, *args, **kwargs):
    if instance.name and not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(create_slug, sender=Hike)
