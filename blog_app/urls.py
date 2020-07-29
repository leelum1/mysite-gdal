from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
]
