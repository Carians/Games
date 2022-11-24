from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Games, GamesReview
from .metadata import getMetaData
from django.db.models import Avg


@receiver(pre_save, sender=GamesReview)
def games_review_pre_save(sender, instance, *args, **kwargs):
    try:
        gameName = instance.gameName_id
        ratio = GamesReview.objects.all().filter(gameName_id=gameName).aggregate(Avg('rate'))
        print(ratio)
        Games.objects.filter(pk=gameName).update(reviewRatio=float(ratio.get('rate__avg')))
    except Exception as e:
        print('Error: game review avg counting failed.')
        print(e)

@receiver(post_save, sender=GamesReview)
def games_review_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.save()

@receiver(pre_save, sender=Games)
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

@receiver(post_save, sender=Games)
def games_post_save(sender, instance,  created, *args, **kwargs):
    if created:
        instance.save()