import uuid
from django.db import models
from django.utils import timezone

# A collection
class Collection(models.Model) : 
	author = models.ForeignKey('auth.user')
	cards = {}

	def addCard(card):
		cards[len(cards)] = card

	def removeCard(card):
		pass

	def moveCard(card):
		pass


# The Card model which represents a user created card
# Each card also has an implicit id value
class Card(models.Model) : 
	author = models.ForeignKey('auth.User')
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


# The user model
class User(models.Model) : 
	first_name = models.CharField(max_length = 32)
	last_name = models.CharField(max_length = 32)
	user_name = models.CharField(max_length = 20)
	password = models.CharField(max_length = 32)
	email = models.EmailField()
	collection = Collection()
	created_date = models.DateTimeField(blank=True,null=True)
	created = False

	def create(self) : 
		self.created = True
		self.created_date = timezone.now()
		self.save()

	def __str__(self) : 
		return self.user_name
