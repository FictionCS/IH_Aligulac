from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .fullData import fullList
from .activeData import players

def matches(request):
	context = {
		'players':fullList
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
		'players':fullList	
	}
	return render(request, 'ALIGULAC/home.html', context)

def about(request):
	return render(request, 'ALIGULAC/about.html')

