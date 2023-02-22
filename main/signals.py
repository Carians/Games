from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Games, GamesReview
from .metadata import getMetaData


@receiver(pre_save, sender=GamesReview)
def games_review_pre_save(sender, instance, *args, **kwargs):
    pass

@receiver(post_save, sender=GamesReview)
def games_review_post_save(sender, instance, created, *args, **kwargs):
    pass

@receiver(pre_save, sender=Games)
def games_pre_save(sender, instance, *args, **kwargs):
    validator = URLValidator()
    try:
        #validator(str(instance.link))
        already_exists = Games.objects.all().filter(link=instance.link).exists()
        print(already_exists)
        if already_exists and instance.pk is None:
            raise ValidationError('This game already exists')
        if not str(instance.link).__contains__('store.steampowered.com'):
            #if statment in case variable request exists then use it and send message error
            if 'request' in locals():
                messages.error(request, 'Nie można zapisać tego adresu URL')
            raise ValueError('Not a valid Steam link')
        else:
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
                #save to database
    except ValidationError as e:
       # super.save()(*args, **kwargs)
        raise ValidationError(str(e))
@receiver(post_save, sender=Games)
def games_post_save(sender, instance,  created, *args, **kwargs):
    if created:
        instance.save()
