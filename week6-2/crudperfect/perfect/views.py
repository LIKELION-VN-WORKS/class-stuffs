from django.shortcuts import render, redirect
from .models import Post, Comment
# Create your views here.
from .forms import PostForm, CommentForm, UserForm

# 로그인 기능 구현
from django.contrib.auth.models import User
from django.contrib import auth

# 페이지 접근 권한 자체 설정
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


@login_required
def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.author = request.user.get_username()
        post.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', {'form': form})


@login_required
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('detail', post.pk)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'post': post, 'form': form})


@login_required
def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', post_pk)


@login_required
def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        post = form.save(commit=False)
        post.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('home')

    else:
        form = UserForm()
        error = "아이디가 이미 존재합니다"
    return render(request, 'registration/signup.html', {'form': form, 'error': error})
