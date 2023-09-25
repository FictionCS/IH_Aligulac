from django.db import models

class Player(models.Model):
	name = models.CharField(max_length=50)
	rating = models.IntegerField()
	winrate = models.CharField(max_length=50)
	rating = models.IntegerField()
	wins = models.IntegerField()
	losses = models.IntegerField()
	rd = models.IntegerField()
	inactive = models.IntegerField()

	# def __str__(self):