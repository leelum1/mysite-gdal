"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap, BlogSitemap, HikeSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'hike': HikeSitemap,
}

urlpatterns = [
    path('cookies/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('googlea70085b6066e71d7.html', views.google_verify, name='verify'),
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('legal/', views.LegalTemplateView.as_view(), name='legal'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('hiking/', include('hike_app.urls')),
    path('watersheds/', include('watershed_app.urls')),
    path('beaches/', include('beach_app.urls')),
    path('blog/', include('blog_app.urls')),
    path('geojournal/', include('geojournal_app.urls')),
    path('steelbands/', include('steelbands_app.urls')),
    path('markdownx/', include('markdownx.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
