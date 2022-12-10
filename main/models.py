from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db import models
import datetime
# Create your models here.

class Games(models.Model):
    title = models.CharField(max_length=150, null=False, blank=True, unique=True)
    description = models.TextField(null=True, blank=True, max_length=500)
    text = models.TextField(null=True, blank=True, max_length=500)
    date_created = models.DateField(default=datetime.date.today, blank=False, null=False, editable=False)
    link = models.URLField(max_length=200, null=False, blank=False)
    imgURL = models.URLField(default='', blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} {self.description}'

class GamesReview(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    gameName = models.ForeignKey(Games, on_delete=models.CASCADE, null=False, default='')
    rate = models.IntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
                                                      ])
    date_created = models.DateField(default=datetime.date.today, blank=False, null=False, editable=False)

    def __str__(self):
        return f'{self.owner} {self.gameName}'

    class Meta:
        unique_together = ['owner', 'gameName']
