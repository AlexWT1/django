import factory
from myproject.blog.models import Post, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')

    @classmethod
    def create(cls, **kwargs):
        # Переопределите метод create() для сохранения пользователя в базу данных
        password = kwargs.pop('password', None)
        user = super().create(**kwargs)
        if password:
            user.set_password(password)
            user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    title = factory.Faker('sentence', nb_words=4)
    description = factory.Faker('paragraph')