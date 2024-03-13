from django.contrib import admin

from apps.blog.models import Comment, User, Post, Like

admin.site.register([Like, Post, User, Comment])