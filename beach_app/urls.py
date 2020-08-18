from django.urls import path
from . import views

app_name = "beach_app"

urlpatterns = [
    path('', views.BeachListView.as_view(), name="list"),
    path('map/', views.BeachMapTemplateView.as_view(), name="map"),
    path('<slug:slug>/', views.BeachDetailView.as_view(), name="detail"),
]
