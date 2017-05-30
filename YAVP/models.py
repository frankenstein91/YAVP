# Create your models here.
from django.db import models


class Continent(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=15)

    def __str__(self):
        return self.Name


class Country(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=35)
    Continent = models.ForeignKey(Continent, blank=False, null=False)
    Flag = models.ImageField(upload_to="Flags/", null=True, blank=True)

    def __str__(self):
        return self.Name


class City(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=170)
    Country = models.ForeignKey(Country, blank=False, null=False)

    def __str__(self):
        return self.Name


class District(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=170)
    City = models.ForeignKey(City, blank=False, null=False)

    def __str__(self):
        return self.Name + " of " + self.City.Name


class Area(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=170)
    Country = models.ForeignKey(Country, null=True, blank=True)

    def __str__(self):
        return self.Name

class Travel(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=170)

    def __str__(self):
        return self.Name


class TravelStop(models.Model):
    StartDate = models.DateTimeField(blank=False, null=False)
    EndDate = models.DateTimeField(blank=True, null=False)
    travel = models.ForeignKey(Travel, blank=True, null=True)
    if not EndDate:
        EndDate = StartDate
