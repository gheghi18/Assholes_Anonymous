from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from main_app.models import Card
from .forms import *

#Whehter or not adding cards is currently allowed
adding_cards = True

# The Homepage
def homepage(request):
	return render(request, 'main_app/homepage.html',{})

def createCard(request):
	if request.method == 'POST' : 
		form = CardForm(request.POST)

		if form.is_valid() : 
			card_text = request.POST['text']
			user = request.user
			
			if (adding_cards) : 
				Card.objects.create(author = user,text = card_text)
				
				print("Card Added to Database!")

			return HttpResponseRedirect('/confirm/')

	else : 
		form = CardForm()
	
	return render(request,'main_app/createCard.html',{'form':form})

def confirm(request):
	return render(request,'main_app/confirm.html',{})

def cards(request):
	return render(request,'main_app/cards.html',{})

def register(request):
	if request.method == 'POST' : 	
		form = RegistrationForm(request.POST)

		if form.is_valid() : 
			newUser = User.objects.create_user(first_name = request.POST['firstName'],last_name = request.POST['lastName'],
				username = request.POST['username'],password = request.POST['password'], email = request.POST['email'])
			newUser.save()

		return HttpResponseRedirect('/confirm/')

	else : 
		form = RegistrationForm()
		
	return render(request,'main_app/register.html',{'form':form})

def login(request):
	if request.method == 'POST' : 
		form = LoginForm(request.POST)

		if form.is_valid() : 
			pass

		return HTTPResponseRedirect('/confirm/')

	else : 
		form = LoginForm()

	return render(request,'main_app/login.html',{'form':form})