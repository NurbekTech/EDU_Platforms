from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return render(request, "home/index.html")

def contacts(request):
    return render(request, "home/contacts.html")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
