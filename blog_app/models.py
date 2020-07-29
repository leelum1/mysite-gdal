from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from multiselectfield import MultiSelectField

# Create your models here.
class Post(models.Model):
    tagChoices = (
        ('house', 'House Projects'),
        ('life', 'Life'),
        ('running', 'Running'),
        ('website', 'Website'),
    )
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField()
    tags = MultiSelectField(choices=tagChoices) #https://pypi.org/project/django-multiselectfield/
    is_private = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='blog_images/', blank=True)
    text = MarkdownxField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_updated']

    def get_absolute_url(self):
        return reverse('blog_app:detail', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

class BlogImage (models.Model):
    blog = models.ForeignKey(Post, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.blog.title


def create_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(create_slug, sender=Post)
