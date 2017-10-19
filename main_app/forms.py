from django import forms
from django.contrib.auth.models import User

class CardForm(forms.Form) :
	text = forms.CharField(widget = forms.Textarea(attrs={'rows':1,'class':'card-text-area','required':True,"placeholder": "Enter some shit!"}),
	 label = "", max_length = 220)
