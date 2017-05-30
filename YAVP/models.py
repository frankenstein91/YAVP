# Create your models here.
from django.db import models


class Continent(models.Model):
    Name = models.CharField(blank=False, null=False, max_length=15)

    def __str__(self):
        return self.Name


class Travel(models.Model):
    StartDate = models.DateField
    EndDate = models.DateField
