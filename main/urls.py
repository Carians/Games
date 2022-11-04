from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
 path('', views.homePageView.as_view(), name="homepage"),
 path('library', views.libraryView.as_view(), name="library"),
 path('api', include('api.urls'))
]