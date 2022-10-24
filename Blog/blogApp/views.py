from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from blogApp.models import Category, Post

# Create your views here.
def home(request):
    posts = Post.objects.all()[:11]
    cats = Category.objects.all()
    data = {
        'posts':posts,
        'cats':cats
    }
    return render(request, 'home.html', data)

    
def urlpost(request, url):
    url = Post.objects.get(url=url)
    cats = Category.objects.all()

    print(url, '-----------------')
    return render(request, 'posts.html', { 'url':url, 'cats':cats }) 
    
def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)

    return render(request, 'catview.html', {'cat':cat, 'posts':posts }) 


def about(request):
    return render(request, 'about.html', {})