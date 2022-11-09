from django.shortcuts import render
from django.views.generic import View, ListView, DetailView


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
    ordering = ['date_created']
    context_object_name = 'games'


class singleGameView(DetailView):
    template_name = 'main/detail_game.html'
    model = Games
    context_object_name = 'game'


class ErrorView(View): # 404 template
    def get(self, request):
        return render(request, 'main/includes/404.html')