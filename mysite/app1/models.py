from __future__ import unicode_literals
from django.db import models
# Create your models here.
class tweets(models.Model):	
	def __str__(self):
		return self.tweet
	tweet = models.CharField(max_length=200)
	
	
