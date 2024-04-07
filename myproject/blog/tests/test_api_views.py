import pytest
from django.urls import reverse
from django.test import Client
from myproject.blog.models import Post
from myproject.blog.forms import CommentForm
from myproject.blog.tests.factories import UserFactory, PostFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def client():
    """Fixture to create a Django client instance."""
    return Client()


@pytest.fixture
def sample_post():
    """Fixture to create a sample post using Factory Boy."""
    return PostFactory()


@pytest.fixture
def user():
    """Fixture to create a user using Factory Boy."""
    return UserFactory.create()


@pytest.mark.parametrize("view_name, expected_status_code", [
    ('post_list', 200),  # Для post_list ожидаем код 200
    ('post_create', 302),  # Для post_create ожидаем код 302
])
def test_authenticated_user_views(client, view_name, user, expected_status_code):
    """Parameterized test for viewing views accessible only to authenticated users."""
    client.force_login(user)
    response = client.get(reverse(view_name))
    assert response.status_code == expected_status_code


def test_post_detail_view(client, sample_post):
    """Тест для представления post_detail."""
    response = client.get(reverse('post_detail', kwargs={'pk': sample_post.pk}))
    assert response.status_code == 200
    assert 'post' in response.context
    assert 'comments' in response.context
    assert isinstance(response.context['form'], CommentForm)


@pytest.mark.parametrize("view_name", [
    ('post_edit', 1),
    ('post_delete', 1),
    ('add_comment_to_post', 1),
])
def test_redirect_unauthenticated_user_views(client, view_name):
    """Parameterized test for redirecting unauthenticated users."""
    view_name, pk = view_name
    response = client.get(reverse(view_name, kwargs={'pk': pk}))
    assert response.status_code == 302
    assert 'login' in response.url
