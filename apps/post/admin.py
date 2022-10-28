from django.contrib import admin
from .models import Post, Tag, Rating, PostImage, Like

admin.site.register([Post, Tag, Rating, PostImage, Like])
