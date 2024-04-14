from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Post, Comment, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User  # Используйте вашу модель User
        fields = ('username', 'password1', 'password2')


# class CustomAuthenticationForm(AuthenticationForm):
#     class Meta(AuthenticationForm.Meta):
#         model = User
#         fields = AuthenticationForm.Meta.fields('username', 'password1', 'password2')
