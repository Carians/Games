from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.db import models
from .metadata import getMetaData

# Create your models here.

class Games(models.Model):
    title = models.CharField(max_length=150, null=False, blank=True)
    description = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    date_created = models.DateField(default=timezone.now, blank=False, null=False)
    link = models.URLField(max_length=200, null=False, blank=False)
    imgURL = models.URLField(default='', blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.description}'

def games_pre_save(sender, instance,  *args, **kwargs):
    instance.imgURL = getMetaData.image(str(instance.link))
    instance.title = getMetaData.title(str(instance.link))

pre_save.connect(games_pre_save, sender=Games)

def games_post_save(sender, instance,  created, *args, **kwargs):
    if created:
        instance.save()
post_save.connect(games_post_save, sender=Games)
