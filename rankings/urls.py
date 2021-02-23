from django.urls import path
from django.urls import path, register_converter

from . import views

urlpatterns = [
    path('', views.home, name='rankings-home'),
    path('matches/', views.matches, name='rankings-matches'),
    path('predictions/', views.predictions, name='rankings-predictions'),
    path('full/', views.full, name='rankings-full'),
    path('about/', views.about, name='rankings-about'),
    path('player/', views.player, name='rankings-player')
    path('player/<int:year>/', views.player, name='rankings-player')
]
