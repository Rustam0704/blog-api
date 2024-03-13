from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.blog.api_enpoints.User.UserRetrieveUpdateDestroy.serailizers import UserRetrieveUpdateDestroySerializer
from apps.blog.models import User


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroySerializer


__all__ = ('UserRetrieveUpdateDestroyView',)
