from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog\index.html', {'posts': posts})

def about(request):
    posts = Post.objects.all()
    return render(request, 'blog/about.html',{'posts': posts})

def blog(request):
    return render(request, 'blog/blog.html')

def contact(request):
    return render(request, 'blog/contact.html')
