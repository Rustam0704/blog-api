from rest_framework.serializers import ModelSerializer

from apps.blog.models import Comment


class CommentListCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'body', 'post')
