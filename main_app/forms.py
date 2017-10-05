from django import forms

class CardForm(forms.Form) :
	text = forms.CharField(widget = forms.Textarea(attrs={'rows':1,'cols':0,'class':'card-text-area','required':True}), label = "", max_length = 100)