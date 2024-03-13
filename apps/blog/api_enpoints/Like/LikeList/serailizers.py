from rest_framework.serializers import ModelSerializer

from apps.blog.models import Like, User


class AuthorSerailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio', 'birthday')


class LikeListSerializer(ModelSerializer):
    author = AuthorSerailizer()
    class Meta:
        model = Like
        fields = ('author', 'post')
