from django.urls import path
from .views import get_posts, post_posts


urlpatterns = [
    path('v1/posts/', get_posts),
    path('v1/post/', post_posts)
]