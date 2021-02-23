from django.urls import path
from django.urls import path, register_converter
from . import converters, views

from . import views

urlpatterns = [
    path('', views.home, name='rankings-home'),
    path('matches/', views.matches, name='rankings-matches'),
    path('predictions/', views.predictions, name='rankings-predictions'),
    path('full/', views.full, name='rankings-full'),
    path('about/', views.about, name='rankings-about'),
    url(r'about/(?P<username>.+)/$', views.about, name="profile")
]
