from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.core.validators import URLValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from .metadata import getMetaData
import datetime
# Create your models here.

class Games(models.Model):
    title = models.CharField(max_length=150, null=False, blank=True)
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
    gameName = models.OneToOneField(Games, on_delete=models.CASCADE, null=False, default='')
    rate = models.IntegerField(default=0, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
                                                      ])
    date_created = models.DateField(default=datetime.date.today, blank=False, null=False, editable=False)

    def __str__(self):
        return f'{self.owner} {self.gameName}'

def games_pre_save(sender, instance,  *args, **kwargs):
    validator = URLValidator()
    try:
        validator(str(instance.link))
        if not instance.imgURL:
            instance.imgURL = getMetaData.image(str(instance.link))
        if not instance.title:
            instance.title = getMetaData.title(str(instance.link))
            #Remove words from title instance
            banned_words = [
                'on Steam',
                'Save',
                'on',
                'Pre-purchase',
                     ]
            for i in range(len(banned_words)):
                instance.title = instance.title.replace(banned_words[i], '')
            #Remove save {ammount}%
            limit = 0
            if '%' in instance.title:
                position = instance.title.find('%')
                print(instance.title[position])
                while instance.title[position-1].isdigit() and limit <= 100:
                    instance.title = instance.title.replace(instance.title[position-1], '')
                    position = instance.title.find('%')
                    limit+=1
                instance.title = instance.title.replace('%', '')
                limit = 0

    except ValidationError as exception:
        print(exception)

pre_save.connect(games_pre_save, sender=Games)

def games_post_save(sender, instance,  created, *args, **kwargs):
    if created:
        instance.save()
post_save.connect(games_post_save, sender=Games)
