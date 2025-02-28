from django.shortcuts import render
from .models import Driver
from .models import Team
from .models import Circuit
def home(request):
    return render(request, "home.html")

def drivers(request):
    all_drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': all_drivers})

def teams(request):
    all_teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': all_teams})

def circuits(request):
    all_circuits = Circuit.objects.all()
    return render(request, 'circuits.html', {'circuits': all_circuits})