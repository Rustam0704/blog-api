from rest_framework.generics import ListCreateAPIView

from apps.blog.api_enpoints.Comment.CommentListCreate.serailizers import CommentListCreateSerializer
from apps.blog.models import Comment


class CommentListCreateView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListCreateSerializer


__all__ = ('CommentListCreateView',)
