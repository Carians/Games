from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
class homePageView(View):
    def get(self, request):
        return render(request, 'main/homepage.html')

#class lobbyView():
#    pass