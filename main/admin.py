from django.contrib import admin

from .models import Games

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created']
    ordering = ['date_created']


admin.site.register(Games, GamesAdmin)