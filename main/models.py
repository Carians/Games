import datetime,uuid

from django.db import models

# Create your models here.

class Games(models.Model):
    game_name = models.CharField(max_length=150, null=False, blank=False)
    date_created = models.DateField(default=datetime.datetime.now(), blank=False, null=False)

    def __str__(self):
        return self.game_name
class Lobby(models.Model):
    lobby_name = models.CharField(max_length=50, null=False)
    date_created = models.DateField(default=datetime.datetime.now(), blank=False, null=False)
    lobby_game = models.ForeignKey(Games, on_delete=models.CASCADE)
    lobby_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.lobby_game

    class Meta:
        ordering = ['lobby_name']