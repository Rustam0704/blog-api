from rest_framework.serializers import ModelSerializer

from apps.blog.models import Like


class LikeDestroySerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ('author', 'post')