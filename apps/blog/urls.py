from django.urls import path
from apps.blog import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<int:post_id>", views.show_post, name="post"),
]
