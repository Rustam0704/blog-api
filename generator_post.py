def main():
    faker = Faker()
    for i in range(20):
        user = User.objects.get(id=random.choice([2, 3, 4]))
        post = Post.objects.create(user=user, title=faker.sentence(), body=faker.text(), is_active=True)
        post.save()


if __name__ == '__main__':
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    application = get_wsgi_application()

    import random

    from faker import Faker

    from apps.blog.models import Post, User
    from django.utils.timezone import datetime

    main()
