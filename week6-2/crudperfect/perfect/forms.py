from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'contents', 'price', 'rating', 'img')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
            'content': (''),
        }

        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 입력하세요'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widget = {
            'password': forms.PasswordInput()
        }
