from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from main_app.models import Card
from .forms import CardForm

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