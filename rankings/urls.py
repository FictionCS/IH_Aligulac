from django.urls import path
from . import views
import playerMatches.py

urlpatterns = [
    path('', views.home, name='rankings-home'),
    path('matches/', views.matches, name='rankings-matches'),
    path('predictions/', views.predictions, name='rankings-predictions'),
    path('full/', views.full, name='rankings-full'),
    path('about/', views.about, name='rankings-about')
]

for player in playerMatches.playerMatches:
	urlpatterns += path('matches/'+player.player, views.about, name='test')