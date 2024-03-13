from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from apps.blog.api_enpoints.Comment import CommentRetrieveUpdateDestroyView, CommentListCreateView
from apps.blog.api_enpoints.Like import LikeListView, LikeCreateView, LikeRetrieveView, LikeUpdateView, LikeDestroyView
from apps.blog.api_enpoints.PasswordUpdate import PasswordUpdateView
from apps.blog.api_enpoints.Post import PostListView, PostCreateView, PostRetrieveView, PostUpdateView, PostDestroyView
from apps.blog.api_enpoints.User import UserListCreateView
from apps.blog.api_enpoints.User.UserRetrieveUpdateDestroy.views import UserRetrieveUpdateDestroyView
# from apps.blog.api_enpoints.Comment.CommentRetrieveUpdateDestroy.views import CommentRetrieveUpdateDestroyView
from apps.blog.views import UserViewSet, PostViewSet, CommentViewSet, Logout

router = DefaultRouter()

# router.register('users', UserViewSet, 'user')
# router.register('posts', PostViewSet, 'posts')
# router.register('comments', CommentViewSet, 'comments')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.obtain_auth_token),
    path('logout/', Logout.as_view()),
    path('comment/<pk>',CommentRetrieveUpdateDestroyView.as_view()),
    path('comment/',CommentListCreateView.as_view()),
    path('like/',LikeListView.as_view()),
    path('like/create/',LikeCreateView.as_view()),
    path('like/<pk>/retrieve', LikeRetrieveView.as_view()),
    path('like/<pk>/update', LikeUpdateView.as_view()),
    path('like/<pk>/destroy', LikeDestroyView.as_view()),
    path('post/',PostListView.as_view()),
    path('post/create/',PostCreateView.as_view()),
    path('post/<pk>/retrieve', PostRetrieveView.as_view()),
    path('post/<pk>/update', PostUpdateView.as_view()),
    path('post/<pk>/destroy', PostDestroyView.as_view()),
    path('user/<pk>',UserRetrieveUpdateDestroyView.as_view()),
    path('user/',UserListCreateView.as_view()),
    path('user/<pk>/updpass', PasswordUpdateView.as_view())
    # path()
    ## user uchun 5ta endpoint
    ## update password apiendpoint
    ## post uchun 5ta endpoint
]
