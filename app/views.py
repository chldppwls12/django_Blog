from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# Create your views here.

def main(request):
    blog = Blog.objects
    return render(request, 'main.html', {'blogs': blog})

def create(request):
    return render(request, 'create.html')

def new(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.directory = request.GET['directory']
    blog.save()
    return redirect('/')

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog': blog})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'update.html', {'blog': blog})

def updat(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.directory = request.GET['directory']
    blog.save()
    return redirect('/')

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()  
    return redirect('/')