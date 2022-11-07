from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'main'
urlpatterns = [
 path('', views.homePageView.as_view(), name="homepage"),
 path('library', views.libraryView.as_view(), name="library"),
 path('api', include('api.urls')),
 path('api/auth', obtain_auth_token),
 path('api/games', views.GamesListCreateAPIView.as_view())
]