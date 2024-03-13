from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.blog.api_enpoints.Comment.CommentRetrieveUpdateDestroy.serailizers import \
    CommentRetrieveUpdateDestroySerailizer
from apps.blog.models import Comment


class CommentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentRetrieveUpdateDestroySerailizer

__all__ = ('CommentRetrieveUpdateDestroyView',)
