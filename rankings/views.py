from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Player

from .fullData import fullList
from .activeData import players
from .playerMatches import playerMatches

def matches(request):
	context = {
		'players':fullList #Player.object.all()
	}
	return render(request, 'ALIGULAC/matches.html', context)

def predictions(request):
	return render(request, 'ALIGULAC/predictions.html')

def full(request):
	context = {
		'players':fullList
	}
	return render(request, 'ALIGULAC/full.html', context)

def home(request):
	context = {
		'players':players	
	}
	return render(request, 'ALIGULAC/home.html', context)

def about(request):
	return render(request, 'ALIGULAC/about.html')

def player(request, playerID='default'):
	if playerID == 'default':
		context = {
			'players':playerMatches
		}
	else:
		context = {
			'players':playerMatches[playerID - 1]
		}
	return render(request, 'ALIGULAC/players.html', context)

