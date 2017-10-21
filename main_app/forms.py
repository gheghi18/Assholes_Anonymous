from django import forms
from django.contrib.auth.models import User

class CardForm(forms.Form) :
	text = forms.CharField(widget = forms.Textarea(attrs={'rows':1,'class':'card-text-area','required':True,"placeholder": "Enter some shit!"}),
	 label = "", max_length = 220)

class RegistrationForm(forms.Form) : 
	firstName = forms.CharField(label="First Name",max_length=30)
	lastName = forms.CharField(label="Last Name",max_length=30)
	email = forms.EmailField()
	username = forms.CharField(label="Username",max_length=25)
	password = forms.CharField(max_length=32, widget=forms.PasswordInput)
