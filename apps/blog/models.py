from django.contrib.auth.models import AbstractUser
from django.db.models import TextField, DateField, Model, CharField, BooleanField, ForeignKey, CASCADE, DO_NOTHING


class Abstract(Model):
    created_at = DateField(auto_now_add=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    birthday = DateField()
    bio = TextField()


class Post(Abstract):
    title = CharField(max_length=128)
    body = TextField()
    is_active = BooleanField(default=False)
    user = ForeignKey(User, CASCADE, 'posts')

    @property
    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return self.title


class Comment(Abstract):
    body = TextField()
    author = ForeignKey(User, CASCADE, 'comments')
    post = ForeignKey(Post, CASCADE, 'comments')

    def __str__(self):
        return self.body


class Like(Abstract):
    author = ForeignKey(User, DO_NOTHING, 'likes')
    post = ForeignKey(Post, CASCADE, 'likes')

    def __str__(self):
        return f"{self.author} {self.post}"

    class Meta:
        unique_together = ['author', 'post']
