from django.db import models
from django.utils import timezone


class Post(models.Model):
    userId = models.BigIntegerField(null=False)
    caseId = models.BigIntegerField(null=False)
    description = models.TextField(null=False)
    createdDate = models.DateTimeField(null=False, default=timezone.now)


class Comment(models.Model):
    userId = models.BigIntegerField(null=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='postComments')
    comment = models.TextField(null=False)
    createdDate = models.DateTimeField(null=False, default=timezone.now)


class PostLike(models.Model):
    userId = models.BigIntegerField(null=False)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='postLikes')
    upvote = models.BooleanField(null=False, default=False)


class CommentLike(models.Model):
    userId = models.BigIntegerField(null=False)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='commentLikes')
    upvote = models.BooleanField(null=False, default=False)
