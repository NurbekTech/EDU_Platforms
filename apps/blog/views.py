from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts })
