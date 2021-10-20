from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Continent(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Country(models.Model):
    name      = models.CharField(max_length=64)
 
    def __str__(self):
        return f"{self.name}"

class League(models.Model):
    name    = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=PROTECT, related_name="league_country")

    def __str__(self):
        return f"{self.name} in {self.country}"

class Team(models.Model):
    name            = models.CharField(max_length=128)
    league          = models.ForeignKey(League, on_delete=PROTECT, related_name="team_league")
    games_played    = models.IntegerField()
    games_won       = models.IntegerField()
    games_lost      = models.IntegerField()
    goals_scored    = models.IntegerField()
    goals_conceded  = models.IntegerField()

    def __str__(self):
        return f""

class Player(models.Model):
    first_name      = models.CharField(max_length=64)
    last_name       = models.CharField(max_length=64)
    Team            = models.ForeignKey(Team, on_delete=PROTECT, related_name="player_team")
    games_played    = models.IntegerField()
    goals_scored    = models.IntegerField()
    goals_conceded  = models.IntegerField()

    def __str__(self):
        return f""