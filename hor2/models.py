from django.db import models
from django.utils import timezone



class Horoscope(models.Model):
	name=models.CharField(max_length=120)
	date=models.DateTimeField(blank=True,default=timezone.now)
	# hour=models.IntegerField(blank=True, default=1)
	# mint=models.IntegerField(blank=True, default=1)
	# lat=models.FloatField(blank=True,default=1)
	# lon=models.FloatField(blank=True,default=1)
	# tzone=models.FloatField(blank=True,default=1)


	def __str__(self):
		return self.name
# Create your models here.