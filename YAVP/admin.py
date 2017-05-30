# Register your models here.
from django.contrib import admin

from YAVP.models import Continent


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    search_fields = ["Name"]
    pass
