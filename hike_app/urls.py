from django.urls import path
from . import views

app_name = "hike_app"

urlpatterns = [
    path('safety/', views.HikeSafetyTemplateView.as_view(), name="safety"),
    path('', views.HikeListView.as_view(), name="list"),
    path('map/', views.HikeMapTemplateView.as_view(), name="map"),
    path('<slug:slug>/', views.HikeDetailView.as_view(), name="detail"),
]
