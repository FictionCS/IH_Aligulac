from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rankings-home'),
    path('about/', views.about, name='ranking-about')
]