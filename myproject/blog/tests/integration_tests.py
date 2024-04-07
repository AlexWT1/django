from django.test import TestCase, Client
from django.urls import reverse

from myproject.blog.forms import CommentForm
from myproject.blog.models import Post, Comment, User


class PostViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='password')
        self.client.force_login(self.user)
        self.post = Post.objects.create(title='Test Post', author=self.user, description='Test Description')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        posts = Post.objects.all()
        expected_posts = [str(post) for post in posts]
        actual_posts = [str(post) for post in response.context['posts']]
        self.assertListEqual(actual_posts, expected_posts)

    def test_post_detail_view(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)
        self.assertIsInstance(response.context['form'], CommentForm)

    def test_post_create_view(self):
        response = self.client.post(reverse('post_create'), {'title': 'New Post', 'description': 'New Description'})
        self.assertEqual(response.status_code, 302)

    def test_post_edit_view(self):
        response = self.client.post(reverse('post_edit', kwargs={'pk': self.post.pk}),
                                    {'title': 'Updated Post', 'description': 'Updated Description'})
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)

    def test_add_comment_to_post_view(self):
        response = self.client.post(reverse('add_comment_to_post', kwargs={'pk': self.post.pk}),
                                    {'text': 'Test Comment'})
        self.assertEqual(response.status_code, 302)
