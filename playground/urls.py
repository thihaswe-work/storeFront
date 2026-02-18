from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/", views.say_hello, name="playground_hello"),
    path("about/", views.about, name="about"),
]
