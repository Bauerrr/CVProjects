from django.contrib import admin
from .models import Post, User, Comment, Hashtag
# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Hashtag)