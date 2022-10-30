from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
 path('', views.homePageView.as_view(), name="homepage"),
# path('/lobby/<str>', views.lobbyView(), name="gameLobby"),

]