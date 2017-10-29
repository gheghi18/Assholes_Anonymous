import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# The Card model which represents a user created card
# Each card also has an implicit id value
class Card(models.Model) : 
	author = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	text = models.CharField(max_length = 400)
	created_date = models.DateTimeField(default=timezone.now)
	published = False
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self) :
		self.published = True
		self.published_date = timezone.now()
		self.save()

	def __str__(self) : 
		return self.text


# A collection
class Collection(models.Model) : 
	author = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	cards = models.ManyToManyField(Card)

	def publish(self) : 
		self.save()

	def removeCard(self,card):
		pass

	def moveCard(self,card):
		pass




