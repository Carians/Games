from django.contrib import admin, messages
from django import forms
from .models import Games, GamesReview

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']
    ordering = ['date_created']

    def save_model(self, request, obj, form, change):
        link = form.cleaned_data.get('link')

        if not str(link).__contains__('store.steampowered.com'):
            messages.add_message(request, messages.ERROR, 'Nie można zapisać tego adresu URL')
            return
        else:
            super().save_model(request, obj, form, change)
            messages.add_message(request, messages.SUCCESS, 'Zmiany zostały zapisane')
    def response_add(self, request, obj):
        messages.set_level(request, messages.ERROR)
        return super().response_add(request, obj)

class GamesReviewAdmin(admin.ModelAdmin):
    list_display = ['owner', 'gameName', 'rate', 'date_created']
    ordering = ['date_created']

admin.site.register(Games, GamesAdmin),
admin.site.register(GamesReview, GamesReviewAdmin)