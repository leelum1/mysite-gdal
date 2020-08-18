from django.urls import path
from . import views

app_name = "geojournal_app"

urlpatterns = [
    path('', views.GeojournalTemplateView.as_view(), name="geojournal"),
    path('create/', views.EntryCreateView.as_view(), name='create'),
    path('map/', views.EntryListView.as_view(), name='list'),
    path('update/<slug:slug>/', views.EntryUpdateView.as_view(), name='update'),
]
