from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rankings-home'),
    path('full/', views.full, name='rankings-full'),
    path('about/', views.about, name='rankings-about')
]