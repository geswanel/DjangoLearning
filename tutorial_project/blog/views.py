from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {"author": "Jane Foster",
     "date_posted": "September 8, 2023",
     "title": "Blog post 1",
     "content": "blog post 1 content"},
    {"author": "Robert Smith",
     "date_posted": "August 10, 2022",
     "title": "Blog post 2",
     "content": "blog post 2 content"},
]

# Create your views here.
def home(request):
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)

def about(request):
    context = {
        "title": "About",
    }
    return render(request, "blog/about.html", context)