from django.urls import path
from .views import *

urlpatterns = [
    path('post', PostList.as_view(), name='postlistcreate'),
    path('post/<int:pk>', PostDetail.as_view(), name='postdetaildestroy'),
    path('comment', CommentList.as_view(), name='commentlistcreate'),
    path('comment/<int:pk>', CommentDetail.as_view(),
         name='commentdetaildestroy'),
    path('postLike', PostLikeList.as_view(), name='postlikelistcreate'),
    path('postLike/<int:pk>', PostLikeDetail.as_view(),
         name='postlikedetaildestroy'),
    path('commentLike', CommentLikeList.as_view(), name='commentlikelistcreate'),
    path('commentLike/<int:pk>', CommentLikeDetail.as_view(),
         name='commentlikedetaildestroy'),
]
