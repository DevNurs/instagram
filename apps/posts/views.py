from django.shortcuts import render, redirect
from apps.posts.models import Post
from apps.comments.models import Comment
from apps.posts.forms import PostForm


def index(request):
    posts = Post.objects.all()
    if 'comment' in request.POST:
        id = request.POST.get('post_id')
        post = Post.objects.get(id=id)
        text = request.POST.get('comment_text')
        comment = Comment.objects.create(text=text, post=post, user=request.user)
        return redirect('index')
    return render(request, 'posts/index.html', {"posts": posts})


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post()
            post.image = form.cleaned_data['image']
            post.owner = request.user
            post.description = form.cleaned_data['description']
            post.save()
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
