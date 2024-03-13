from rest_framework.serializers import ModelSerializer

from apps.blog.models import Comment, User


class MiniAuthorSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'bio', 'birthday')


class CommentRetrieveUpdateDestroySerailizer(ModelSerializer):
    author = MiniAuthorSerializer()

    class Meta:
        model = Comment
        fields = ('author', 'body', 'post')
