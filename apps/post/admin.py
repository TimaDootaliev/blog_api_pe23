from django.contrib import admin
from .models import Post, Tag, Rating

admin.site.register([Post, Tag, Rating])
