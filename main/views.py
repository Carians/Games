from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView

from .models import Games

# Create your views here.
class homePageView(View):
    def get(self, request):
        games = Games.objects.all().order_by('-date_created')[:3]
        return render(request, 'main/main.html', {
            'games': games
        })


class libraryView(ListView):
    template_name = 'main/library.html'
    model = Games
    ordering = ['date']
    context_object_name = 'games'