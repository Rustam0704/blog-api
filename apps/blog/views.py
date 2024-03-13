from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.filters import OrderingFilter

from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet

from apps.blog.models import User, Post, Comment, Like
from apps.blog.paginations import Page10NumberPagination
from apps.blog.permissions import IsSuperUser, IsOwner
from apps.blog.serailizers import UserCreateSerializer, UserListSerializer, PostSerializer, CommentSerializer, \
    PostDetailSerializer, CommentCreateSerializer, LikeSerializer


class UserViewSet(ViewSet):
    permission_classes = [IsSuperUser, ]

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'detail': 'User registered'}, status=status.HTTP_201_CREATED)
        else:
            return Response(data={'detail': 'something went wring'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserListSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


from rest_framework.decorators import action


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # permission_classes = [IsSuperUser,]

    @action(detail=True, methods=['post'], url_path='press-like')
    def like_post(self, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        like = Like.objects.create(post=post, author=user)
        serializer = LikeSerializer(like)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='dislike')
    def dislike_post(self, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        like = get_object_or_404(Like, author=user, post=post)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset

    def retrieve(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostDetailSerializer(post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_fields = ('body', 'author__username', 'post__title')
    ordering_fields = ['post__likes', 'id', '-id']
    search_fields = ('body', 'post__title', 'author__username')
    pagination_class = Page10NumberPagination

    def create(self, request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
