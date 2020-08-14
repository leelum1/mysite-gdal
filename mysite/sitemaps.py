from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog_app.models import Post
from hike_app.models import Hike

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['index',
                'legal',
                'contact',
                'blog_app:list',
                'watershed_app:map']

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def location(self, item):
        return reverse('blog_app:detail', args=[str(item.slug)])


class HikeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Hike.objects.all()

    def location(self, item):
        return reverse('hike_app:detail', args=[str(item.slug)])
