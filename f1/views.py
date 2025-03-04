"""Views for the F1 Django application."""

from django.shortcuts import render
from .models import Driver, Team, Circuit

def home(request):
    """Render the home page."""
    return render(request, "home.html")

def drivers(request):
    """Retrieve all drivers and render the drivers page."""
    all_drivers = Driver.objects.all()
    return render(request, 'drivers.html', {'drivers': all_drivers})

def teams(request):
    """Retrieve all teams and render the teams page."""
    all_teams = Team.objects.all()
    return render(request, 'teams.html', {'teams': all_teams})

def circuits(request):
    """Retrieve all circuits and render the circuits page."""
    all_circuits = Circuit.objects.all()
    return render(request, 'circuits.html', {'circuits': all_circuits})
