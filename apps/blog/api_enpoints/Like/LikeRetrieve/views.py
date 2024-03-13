from rest_framework.generics import RetrieveAPIView

from apps.blog.api_enpoints.Like.LikeRetrieve.serailizers import LikeRetrieveSerializer
from apps.blog.models import Like


class LikeRetrieveView(RetrieveAPIView):
    serializer_class = LikeRetrieveSerializer
    queryset = Like.objects.all()


__all__ = ('LikeRetrieveView',)
