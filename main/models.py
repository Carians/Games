from django.utils import timezone
from django.db import models

# Create your models here.

class Games(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    date_created = models.DateField(default=timezone.now, blank=False, null=False)
    link = models.URLField(max_length=200, null=False, blank=False)
    imgURL = models.URLField()

    def __str__(self):
        return f'{self.title} {self.description}'
