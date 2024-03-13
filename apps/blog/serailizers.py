from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.blog.models import User, Post, Comment, Like


class UserCreateSerializer(ModelSerializer):
    password1 = serializers.CharField(max_length=128, write_only=True)
    password2 = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'bio', 'birthday', 'username', "password1", "password2")

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise ValidationError('passwords did not match')

        return attrs

    def validate_username(self, value):
        if not value.isalpha():
            raise ValidationError("username must contains only letters")
        return value

    def create(self, validated_data):
        password = validated_data['password1']
        username = validated_data['username']
        birthday = validated_data['birthday']
        bio = validated_data['bio']
        user = User.objects.create(username=username, bio=bio, birthday=birthday)
        user.set_password(password)
        user.save()
        return user


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'birthday')


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'is_active', 'body', 'user', 'like_count')


class CommentSerializer(ModelSerializer):
    author = UserListSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = ('id','body', 'author', 'post', "created_at")


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('body', 'post', "created_at")




class PostDetailSerializer(ModelSerializer):
    comments = CommentCreateSerializer(many=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'is_active', 'user', 'comments')


class MiniUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MiniPostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title')


class LikeSerializer(ModelSerializer):
    author = MiniUserSerializer()
    post = MiniPostSerializer()

    class Meta:
        model = Like
        fields = ('author', 'post', 'created_at')
