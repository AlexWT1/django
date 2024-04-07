from django.test import TestCase
from django.contrib.auth.models import User
from myproject.blog.models import User, Comment, Post


class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='test_user', email='test@example.com', password='12345')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('12345'))


class PostModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        cls.test_user = User.objects.create(username='test_user', password='password')

    def test_post_creation(self):
        # Создаем объект поста и присваиваем значения его атрибутам
        post = Post(author=self.test_user, title='Test Title', description='Test Description')
        # Сохраняем объект поста
        post.save()
        # Проверяем, что пост создан успешно
        self.assertIsNotNone(post)


class CommentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        cls.test_user = User.objects.create(username='test_user', password='password')
        # Создаем тестовый пост
        cls.test_post = Post.objects.create(author=cls.test_user, title='Test Post', description='Test Description')

    def test_comment_creation(self):
        # Создаем комментарий
        comment = Comment.objects.create(post=self.test_post, author=self.test_user, text='Test Comment')
        # Проверяем, что комментарий был успешно создан
        self.assertIsNotNone(comment)
        # Проверяем связь с постом
        self.assertEqual(comment.post, self.test_post)
        # Проверяем связь с автором
        self.assertEqual(comment.author, self.test_user)
        # Проверяем текст комментария
        self.assertEqual(comment.text, 'Test Comment')
