from django.urls import path
from . import views

urlpatterns = [
 path('', views.homePageView.as_view(), name="homepage"),
# path('/lobby/<str>', views.lobbyView(), name="gameLobby"),

]