from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    headquarters = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    championships = models.IntegerField(default=0)
    logo = models.ImageField(upload_to="team_logos/", null=True, blank=True)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    nationality = models.CharField(max_length=50)
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="drivers"
    )
    wins = models.IntegerField(default=0)
    podiums = models.IntegerField(default=0)
    poles = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="driver_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.number})"


class Circuit(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date = models.DateField()
    winner = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name="circuit_wins")
    image = models.ImageField(upload_to="circuit_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
