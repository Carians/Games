from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homePageView.as_view(), name="homepage"),
    path('library', views.libraryView.as_view(), name="library"),
    path('library/<int:pk>', views.singleGameView.as_view(), name='game_detail'),
    path('api/games', views.GamesListCreateAPIView.as_view()),
    path('api/games/<int:pk>/update', views.GamesUpdateAPIView.as_view()),
    path('api/games/<int:pk>/delete', views.GamesDeleteAPIView.as_view()),
    path('api/games/<int:pk>/', views.GamesDetailAPIView.as_view()),
]