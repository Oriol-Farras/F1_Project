from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('pilotos/', views.drivers, name='drivers'),
    path('equipos/', views.teams, name='teams'),
    path('circuitos/', views.circuits, name='circuits'),
]