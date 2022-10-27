from django.contrib import admin
from .models import Post, Tag, Rating, PostImage

admin.site.register([Post, Tag, Rating, PostImage])
