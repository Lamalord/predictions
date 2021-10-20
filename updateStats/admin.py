from django.contrib import admin
from .models import Continent, Country, League, Team, Player

# Register your models here.
admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)