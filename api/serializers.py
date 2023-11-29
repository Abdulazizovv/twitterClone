from rest_framework import serializers
from main.models import Tweet


class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'

class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'content')
