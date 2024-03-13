from rest_framework.generics import DestroyAPIView

from apps.blog.api_enpoints.Post.PostDestroy.serailizers import PostDestroySerializer
from apps.blog.models import Post


class PostDestroyView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDestroySerializer


__all__ = ("PostDestroyView",)
