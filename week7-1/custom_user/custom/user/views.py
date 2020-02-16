from django.shortcuts import render, redirect
from .models import Post, Comment, User
# Create your views here.
# 변경된 사안 UserCreationForm, UserChangeForm
from .forms import PostForm, CommentForm, UserCreationForm, UserChangeForm


# 페이지 접근 권한 자체 설정
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView


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


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
