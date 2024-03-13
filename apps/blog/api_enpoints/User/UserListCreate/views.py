from rest_framework.generics import ListCreateAPIView

from apps.blog.api_enpoints.User.UserListCreate.serailizers import UserListCreateSerializer
from apps.blog.models import User


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListCreateSerializer


__all__ = ('UserListCreateView',)
