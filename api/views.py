from django.shortcuts import render
from rest_framework import generics
from board.models import *
from .serializers import *

# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().prefetch_related('postComments', 'postLikes')
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all().prefetch_related('postComments', 'postLikes')
    serializer_class = PostSerializer
    pass


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().prefetch_related(
        'nestedComments', 'commentLikes')
    serializer_class = CommentSerializer
    pass


class CommentDetail(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all().prefetch_related(
        'nestedComments', 'commentLikes')
    serializer_class = CommentSerializer
    pass


class PostLikeList(generics.ListCreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    pass


class PostLikeDetail(generics.RetrieveDestroyAPIView):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer
    pass


class CommentLikeList(generics.ListCreateAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    pass


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    queryset = CommentLike.objects.all()
    serializer_class = CommentLikeSerializer
    pass
