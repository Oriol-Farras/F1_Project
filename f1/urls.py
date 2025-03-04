"""URL configuration for the F1 Django application."""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pilotos/', views.drivers, name='drivers'),
    path('equipos/', views.teams, name='teams'),
    path('circuitos/', views.circuits, name='circuits'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
