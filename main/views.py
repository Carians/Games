from django.shortcuts import render
from django.views.generic import View, ListView

from rest_framework import generics, authentication, permissions
#
from .models import Games
from .serializers import GameSerializer
from .permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication

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

class GamesListCreateAPIView(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
        ]

    queryset = Games.objects.all()
    serializer_class = GameSerializer

    # def perform_create(self, serializer):

class GamesDeleteAPIView(generics.DestroyAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer

    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class GamesUpdateAPIView(generics.UpdateAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    lookup_field = 'pk'

class GamesDetailAPIView(generics.RetrieveAPIView):
    queryset = Games.objects.all()
    serializer_class = GameSerializer