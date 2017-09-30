from django.contrib import admin
from .models import Post

# This makes our model visible on the admin page
admin.site.register(Post)