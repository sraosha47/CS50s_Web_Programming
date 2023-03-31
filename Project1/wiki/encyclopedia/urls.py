from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name="newpage"),
    path("random", views.random, name="random"),
    path("<str:entry>", views.wiki, name="wiki"),
]
