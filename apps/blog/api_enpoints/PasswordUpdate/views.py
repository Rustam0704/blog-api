from rest_framework.generics import UpdateAPIView

from apps.blog.api_enpoints.PasswordUpdate.serializers import PasswordUpdateSerializer
from apps.blog.models import User


class PasswordUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = PasswordUpdateSerializer


__all__ = ('PasswordUpdateView',)
