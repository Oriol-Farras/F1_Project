from django.shortcuts import render
from .models import Driver
def home(request):
    return render(request, "home.html")

def drivers(request):
    all_drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': all_drivers})

def teams(request):
    return render(request, 'teams.html')

def circuits(request):
    return render(request, 'circuits.html')