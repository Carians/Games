from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from rest_framework import generics, authentication, permissions
from api.mixins import StaffEditorPermissionMixin
#
from .models import Games, GamesReview
from .serializers import GameSerializer, GamePUTSerializer, GameReviewSerializer, GameReviewPUTSerializer
from .permissions import IsStaffEditorPermission

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_searchable'] = True
        return context


class singleGameView(DetailView):
    template_name = 'main/detail_game.html'
    model = Games
    context_object_name = 'game'

    #On view call incement views in Games model
    def get_object(self):
        pk = self.kwargs.get('pk')
        game_object = Games.objects.get(pk=pk)
        game_object.views = game_object.views+1
        game_object.save()
        return game_object

class ErrorView(View): # 404 template
    def get(self, request):
        return render(request, 'main/includes/404.html')

class GamesListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView,
):

    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GamesDeleteAPIView(
    generics.DestroyAPIView,
    StaffEditorPermissionMixin
                            ):

    queryset = Games.objects.all()
    serializer_class = GameSerializer

    lookup_field = 'pk'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class GamesUpdateAPIView(generics.UpdateAPIView,
                        StaffEditorPermissionMixin
                         ):
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    queryset = Games.objects.all()
    serializer_class = GamePUTSerializer

    lookup_field = 'pk'
    def perform_update(self, serializer):
        serializer.save()



class GamesDetailAPIView(generics.RetrieveAPIView,
                         StaffEditorPermissionMixin
                         ):

    queryset = Games.objects.all()
    serializer_class = GameSerializer

class GamesReviewListCreateAPIView(
    generics.ListCreateAPIView,
    StaffEditorPermissionMixin,
):
    def get_queryset(self, *args, **kwargs):
        return GamesReview.objects.all().filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    serializer_class = GameReviewSerializer

class GamesReviewDeleteAPIView(
    generics.DestroyAPIView,
    StaffEditorPermissionMixin
                            ):

    lookup_field = 'gameName'

    def get_queryset(self, *args, **kwargs):
        return GamesReview.objects.all().filter(owner=self.request.user)

    serializer_class = GameReviewSerializer

    lookup_field = 'gameName'
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

class GamesReviewUpdateAPIView(generics.UpdateAPIView,
                        StaffEditorPermissionMixin
                         ):

    lookup_field = 'gameName'

    def get_queryset(self, *args, **kwargs):
        return GamesReview.objects.all().filter(owner=self.request.user)
    serializer_class = GameReviewPUTSerializer

class GamesReviewDetailAPIView(generics.RetrieveAPIView,
                         StaffEditorPermissionMixin
                         ):

    def get_queryset(self, *args, **kwargs):
        return GamesReview.objects.all().filter(owner=self.request.user)

    serializer_class = GameReviewSerializer

    lookup_field = 'gameName'

