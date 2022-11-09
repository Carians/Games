from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homePageView.as_view(), name="homepage"),
    path('library', views.libraryView.as_view(), name="library"),
    path('library/<int:pk>', views.singleGameView.as_view(), name='game_detail')
]

# handler404 = views.ErrorView.as_view()