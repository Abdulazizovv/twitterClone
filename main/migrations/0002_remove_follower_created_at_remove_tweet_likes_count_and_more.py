# Generated by Django 4.2.7 on 2023-11-13 11:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='likes_count',
        ),
        migrations.RemoveField(
            model_name='tweet',
            name='retweets_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_image_url',
        ),
        migrations.AddField(
            model_name='tweet',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='tweet_comments', to='main.comment'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=280),
        ),
    ]
