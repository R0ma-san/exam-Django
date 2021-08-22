from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post
from .forms import PostForm
from django.http.response import HttpResponseNotFound
from django.contrib.auth import get_user_model

User = get_user_model()

def post(request):

    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts': posts})

def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/my_posts.html', {'posts': posts})

def post_detail(request, pk):
    post_detail = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post_detail': post_detail})

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})

def post_delete(request, pk):
    
    try:
        post = Post.objects.get(id=pk)
        post.delete()
        return redirect('posts')
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Пост не найдена</h2>")