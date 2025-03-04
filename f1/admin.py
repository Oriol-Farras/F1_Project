"""Admin panel configuration for managing Team, Driver, and Circuit models."""

from django.contrib import admin
from .models import Team, Driver, Circuit

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Manages the admin view for teams."""
    list_display = ("name", "headquarters", "engine", "championships")
    search_fields = ("name", "engine")
    list_filter = ("engine",)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    """Manages the admin view for drivers."""
    list_display = ("name", "number", "nationality", "team", "wins", "podiums", "poles")
    search_fields = ("name", "team__name")
    list_filter = ("team", "nationality")

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    """Manages the admin view for circuits."""
    list_display = ("name", "location", "date", "winner")
    search_fields = ("name", "location")
    list_filter = ("date",)
