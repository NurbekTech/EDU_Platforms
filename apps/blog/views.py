from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    cats = Category.objects.all()

    date = {"posts": posts, "cats": cats}
    return render(request, "blog/blog.html", context=date)


def show_post(request, post_id):
    return HttpResponse(f"<h1>Пост но id {post_id}<h1/>")


def show_category(request, cat_id):
    posts = Post.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    
    date = {"posts": posts, "cats": cats}
    return render(request, "blog/blog.html", context=date)
