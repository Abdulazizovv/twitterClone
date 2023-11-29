from django.contrib.auth.models import User
from django.db import models



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    verify = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/default.png')

    def __str__(self):
        return self.user.username
    

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField('UserProfile', related_name='tweet_likes', blank=True)
    comments = models.ManyToManyField('Comment', related_name='tweet_comments', blank=True)
    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}..."

class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Retweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on {self.tweet.user.username}'s tweet"
