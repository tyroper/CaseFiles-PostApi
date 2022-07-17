from asyncore import read
from rest_framework import serializers
from board.models import *


class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = ('id', 'comment', 'userId', 'upvote')


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('id', 'post', 'userId', 'upvote')


class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    def get_likes(self, comment):
        upvotes = comment.commentLikes.all().filter(upvote=True).count()
        downvotes = comment.commentLikes.all().filter(upvote=False).count()
        return upvotes - downvotes

    class Meta:
        model = Comment
        fields = ('id', 'post', 'userId', 'comment',
                  'createdDate', 'likes')


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    postComments = CommentSerializer(many=True, read_only=True)

    def get_likes(self, post):
        upvotes = post.postLikes.all().filter(upvote=True).count()
        downvotes = post.postLikes.all().filter(upvote=False).count()
        return upvotes - downvotes

    class Meta:
        model = Post
        fields = ('id', 'userId', 'caseId',
                  'description', 'createdDate', 'likes', 'postComments')
