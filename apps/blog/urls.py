from django.urls import path
from apps.blog import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<slug:post_slug>", views.show_post, name="post"),
    path("cats/<int:cat_id>", views.show_category, name="category"),
]
