from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main_app.models import Card,Collection
from .forms import *

#Whehter or not adding cards is currently allowed
adding_cards = True

# The Homepage
def homepage(request):
	return render(request, 'main_app/homepage.html',{})

@login_required(login_url = "/login/")
def createCard(request):
	if request.method == 'POST' : 
		form = CardForm(request.POST)

		if form.is_valid() : 
			card_text = request.POST['text']
			user = request.user
			
			if (adding_cards) : 
				card = Card.objects.create(author = user,text = card_text)
				card.publish()
				Collection.objects.get(author = request.user).cards.add(card)
				Collection.objects.get(author = request.user).save()
				print("Card Added to Database!")

			return HttpResponseRedirect('/confirm/')

	else : 
		form = CardForm()
	
	return render(request,'main_app/createCard.html',{'form':form})

def confirm(request):
	return render(request,'main_app/confirm.html',{})

@login_required(login_url = "/login/")
def cards(request):
	collection = getUserCollection(request)

	if (len(collection) == 0) : 
		collection = 0

	if collection != None : 
		print(collection)
		return render(request,'main_app/cards.html',{'collection':collection})
	
	else : 
		return render(request,'main_app/cards.html',{})

def community(request) : 
	return render(request,'main_app/community.html',{})

def official_collection(request) : 
	# You have to send in the official collection
	collection = Collection.objects.get(author = User.objects.get(username = "Assholes")).cards.all()
	return render(request,'main_app/official-collection.html',{'collection':collection})

def register(request):
	if request.method == 'POST' : 	
		form = RegistrationForm(request.POST)

		if form.is_valid() : 
			newUser = User.objects.create_user(first_name = request.POST['firstName'],last_name = request.POST['lastName'],
				username = request.POST['username'],password = request.POST['password'], email = request.POST['email'])
			newUser.save()
			userCollection = Collection.objects.create()
			userCollection.author = newUser
			userCollection.publish()


		return HttpResponseRedirect('/confirm/')

	else : 
		form = RegistrationForm()
		
	return render(request,'main_app/register.html',{'form':form})

def userlogin(request):
	if request.method == 'POST' : 
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username = username, password = password)
		
		if user is not None :
			login(request,user)
			print("Login Succsessful!")
			return HttpResponseRedirect('/confirm/')
		
		else : 
			print("Login Unsuccsessful")
			form = LoginForm()
			return render(request,'main_app/login.html',{'form':form})

	else : 
		form = LoginForm()

	return render(request,'main_app/login.html',{'form':form})

def userlogout(request) :
	logout(request)
	return HttpResponseRedirect('/confirm/')

def getUserCollection(request) : 
	if request.user is not None :
		return Collection.objects.get(author = request.user).cards.all()
	else :
		return None
