from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="blog-home"),  # naming?
    path("about/", views.about, name="blog-about")
]