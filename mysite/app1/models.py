from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.question_text
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('Date published')
class Choices(models.Model):
	def __str__(self):
		return self.choice_text
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
#model to store tweets and display them
class tweets(models.Model):	
	def __str__(self):
		return self.tweet
	tweet = models.CharField(max_length=200)
class topnames(models.Model):
	def __str__(self):
		return self.names
	names = models.CharField(max_length=200)
	count = models.IntegerField(default=0)
	
	
