from django.urls import path
from . import views

app_name = "watershed_app"

urlpatterns = [
    path('map/', views.WatershedMapTemplateView.as_view(), name="map"),
]
