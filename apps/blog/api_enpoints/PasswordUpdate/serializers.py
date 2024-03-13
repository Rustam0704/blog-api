from rest_framework.serializers import ModelSerializer

from apps.blog.models import User


class PasswordUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password',)
