from django.shortcuts import render
from django.utils import timezone

# Create your views here.
def homepage(request):
	return render(request, 'main_app/homepage.html',{})