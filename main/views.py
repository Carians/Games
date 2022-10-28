from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .models import Games
from .metadata import getMetaData

# Create your views here.
class homePageView(View):
    def get(self, request):
        games = Games.objects.all().order_by('date_created')[:3]
        return render(request, 'main/main.html', {
            'games': games
        })


