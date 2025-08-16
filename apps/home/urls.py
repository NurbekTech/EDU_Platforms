from django.urls import path
from apps.home import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contacts/", views.contacts, name="home_contacts"),
]
