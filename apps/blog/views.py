from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


# Create your views here.
def blog(request):
    posts = Post.objects.all()

    date = {"posts": posts}
    return render(request, "blog/blog.html", context=date)


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, "blog/show_post.html", {"post": post})


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    date = {"posts": posts}
    return render(request, "blog/blog.html", context=date)
