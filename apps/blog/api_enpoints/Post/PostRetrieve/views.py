from rest_framework.generics import RetrieveAPIView

from apps.blog.api_enpoints.Post.PostRetrieve.serailizers import PostRetrieveSerializer
from apps.blog.models import Post


class PostRetrieveView(RetrieveAPIView):
    serializer_class = PostRetrieveSerializer
    queryset = Post.objects.all()


__all__ = ('PostRetrieveView',)
