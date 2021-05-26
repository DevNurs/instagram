from django.shortcuts import render, redirect
from apps.posts.models import Post
from apps.posts.forms import PostForm


def index(request):
    posts = Post.objects.all()
    return render(request, 'posts/index.html', {"posts": posts})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {"post": post})


def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post.image = form.cleaned_data['image']
            post.description = form.cleaned_data['description']
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'posts/update.html', {'form': form})


def delete(request, id):
    if request.method == 'POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('index')
    return render(request, 'posts/delete.html')
