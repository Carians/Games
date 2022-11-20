from django.contrib import admin

from .models import Games, GamesReview

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']
    ordering = ['date_created']

class GamesReviewAdmin(admin.ModelAdmin):
    list_display = ['owner', 'gameName', 'rate', 'date_created']
    ordering = ['date_created']

admin.site.register(Games, GamesAdmin),
admin.site.register(GamesReview, GamesReviewAdmin)