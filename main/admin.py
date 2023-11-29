from django.contrib import admin
from .models import Tweet, Like, Retweet, Comment, Follower, UserProfile
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Tweet)
admin.site.register(Retweet)
admin.site.register(Comment)
admin.site.register(Follower)
admin.site.register(Like)