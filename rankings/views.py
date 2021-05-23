from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Player

from .fullData import fullList
from .activeData import players
from .playerMatches import playerMatches
from .tourneyMatches import tourneyMatches

def matches(request):
	context = {
		'players':tourneyMatches
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
	if playerID == '' or not isInt(playerID):
		context = {
			'players':playerMatches
		}
	else:
		context = {
			'players':playerMatches[playerID - 1]
		}
	return render(request, 'ALIGULAC/players.html', context)

def HoF(request):
	context = {'players' : [{'rank': 1, 'player': 'Hoshino', 'rating': 1861},{'rank': 2, 'player': 'Saturas', 'rating': 1695},{'rank': 3, 'player': 'Noah', 'rating': 1684},{'rank': 4, 'player': 'Aicad', 'rating': 1591},{'rank': 5, 'player': 'SenpaiTorpidDow', 'rating': 1563},{'rank': 6, 'player': 'Venaqus', 'rating': 1510},{'rank': 7, 'player': 'No02', 'rating': 1507},{'rank': 8, 'player': 'WellplayedTV', 'rating': 1504},{'rank': 9, 'player': 'Xyr0N', 'rating': 1465},{'rank': 10, 'player': 'Seemann Aiobe', 'rating': 1461}]}
	return render(request, 'ALIGULAC/HoF.html', context)

def records(request):
	context = {'players' : [{'rank': 1, 'player': 'Hoshino', 'rating': 1861},{'rank': 2, 'player': 'Saturas', 'rating': 1695},{'rank': 3, 'player': 'Noah', 'rating': 1684},{'rank': 4, 'player': 'Aicad', 'rating': 1591},{'rank': 5, 'player': 'SenpaiTorpidDow', 'rating': 1563},{'rank': 6, 'player': 'Venaqus', 'rating': 1510},{'rank': 7, 'player': 'No02', 'rating': 1507},{'rank': 8, 'player': 'WellplayedTV', 'rating': 1504},{'rank': 9, 'player': 'Xyr0N', 'rating': 1465},{'rank': 10, 'player': 'Seemann Aiobe', 'rating': 1461}]}
	return render(request, 'ALIGULAC/records.html', context)

def isInt(s):
    try: 
        x = int(s)
        return True
    except ValueError:
        return False