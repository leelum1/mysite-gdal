from django.urls import path
from . import views

app_name = 'steelbands_app'

urlpatterns = [
    path('', views.SteelbandsTemplateView.as_view(), name='steelbands'),
]
