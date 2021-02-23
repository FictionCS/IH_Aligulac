from django.urls import path
from . import views

from .playerMatches import playerMatches

urlpatterns = [
    path('', views.home, name='rankings-home'),
    path('matches/', views.matches, name='rankings-matches'),
    path('predictions/', views.predictions, name='rankings-predictions'),
    path('full/', views.full, name='rankings-full'),
    path('about/', views.about, name='rankings-about')
]
for player in playermatches:
	urlpatterns.append(path(player.player+'/', views.about, name='rankings-'+player.player))