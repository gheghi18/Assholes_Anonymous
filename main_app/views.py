from django.shortcuts import render
from django.utils import timezone

# The Homepage
def homepage(request):
	return render(request, 'main_app/homepage.html',{})

def createCard(request):
	return render(request,'main_app/createCard.html',{})