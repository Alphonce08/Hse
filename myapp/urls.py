from . import views
from django.urls import path

urlpatterns = [
path('', views.index, name='index'),
path('header/', views.name, name='header'),
path('footer/', views.name, name='footer'),
]