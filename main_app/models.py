import uuid
from django.db import models
from django.utils import timezone


# The Card model which represents a user created card
# Each card also has an implicit id value
class Card(models.Model) : 
	author = models.ForeignKey('auth.User')
	text = models.CharField(max_length = 400)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True,null=True)

	def publish(self) :
		self.published_date = timezone.now()
		self.save()

	def __str__(self) : 
		return self.text
