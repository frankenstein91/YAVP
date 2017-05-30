# Register your models here.
from django.contrib import admin

from YAVP.models import *


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    search_fields = ["Name"]
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ["Name"]
    list_filter = ["Continent"]
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ["Name"]
    list_filter = ["Country", "Country__Continent"]
    pass


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    search_fields = ["Name"]
    list_filter = ["City", "City__Country__Continent", "City__Country"]
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ["Name"]
    list_filter = ["Country", "Country__Continent"]
    pass


@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    pass
