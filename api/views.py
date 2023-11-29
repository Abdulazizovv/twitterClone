from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Tweet
from .serializers import PostsSerializer, CreatePostSerializer


@api_view(['GET'])
def get_posts(request):
    posts = Tweet.objects.all()
    serializer = PostsSerializer(posts, many=True)
    return Response(serializer.data, status=202)


@api_view(['POST', 'GET'])
def post_posts(request):
    serializer = CreatePostSerializer()
    if request.method == 'POST':
        if request.user.is_authenticated:
            user = request.user
            content = request.POST.get('content')
            if serializer.is_valid():
                serializer.save(commit=False)
                serializer = serializer(user=user, content=content)
                serializer.save()
                return Response({"Succes: ok"}, status=201)
            else:
                return Response(serializer.errors, status=404)
        else:
            return Response({'error': 'You are not authenticated'})

