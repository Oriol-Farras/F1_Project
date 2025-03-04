from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),
    path('pilotos/', views.drivers, name='drivers'),
    path('equipos/', views.teams, name='teams'),
    path('circuitos/', views.circuits, name='circuits'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)