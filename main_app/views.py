from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def homepage(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
	return render(request, 'main_app/homepage.html', {'posts':posts})