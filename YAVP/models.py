# Create your models here.
from django.db import models


class Travel(models.Model):
    StartDate = models.DateField
    EndDate = models.DateField
