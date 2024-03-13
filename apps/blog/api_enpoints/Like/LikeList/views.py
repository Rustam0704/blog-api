from rest_framework.generics import ListAPIView

from apps.blog.api_enpoints.Like.LikeList.serailizers import LikeListSerializer
from apps.blog.models import Like


class LikeListView(ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeListSerializer


__all__ = ('LikeListView',)
