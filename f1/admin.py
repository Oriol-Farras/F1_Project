from django.contrib import admin
from .models import Team, Driver, Circuit

admin.site.register(Team)
admin.site.register(Driver)
admin.site.register(Circuit)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "headquarters", "engine", "championships")
    search_fields = ("name", "engine")
    list_filter = ("engine",)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "nationality", "team", "wins", "podiums", "poles")
    search_fields = ("name", "team__name")
    list_filter = ("team", "nationality")

@admin.register(Circuit)
class CircuitAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "date", "winner")
    search_fields = ("name", "location")
    list_filter = ("date",)
