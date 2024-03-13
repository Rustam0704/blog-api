from rest_framework.serializers import ModelSerializer

from apps.blog.models import User, Post


class AuthorSeriailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio', 'birthday')


class PostListSerializer(ModelSerializer):
    user = AuthorSeriailizer()
    class Meta:
        model = Post
        fields = ('title', 'body', 'is_active', 'user')
