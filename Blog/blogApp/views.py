from audioop import reverse
from email import message
from pyexpat.errors import messages
from urllib import response
from xml.etree.ElementTree import Comment
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from blogApp.models import Category, Post, Comment

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User

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
    if request.method=='POST':
        # Fetch data from form
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        post = request.POST.get('post')

        print('===>>>', post)

        # set data in objects
        c = Comment()
        c.name=name
        c.email=email
        c.body=body
        # save data in a database
        c.save()
        return redirect('/')
    
    url = Post.objects.get(url=url)
    cats = Category.objects.all()
 
    return render(request, 'posts.html', { 'url':url, 'cats':cats }) 
    
def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)

    return render(request, 'catview.html', {'cat':cat, 'posts':posts }) 


def about(request):
    return render(request, 'about.html', {})


#Auth
def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']

        user = authenticate(request, username=number, password=password)
            
        if user is not None:
            auth_login(request, user)
            messages.success(request, ' Successfully Login')
            return redirect('/')
        else:
            messages.error(request, ' Something Went Wrong')
            return redirect('/login')
            
    return render(request, 'auth/login.html', {})


def logout(request):
    auth_logout(request)
    messages.success(request, ' Logout Successfully')
    return redirect('/')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        number_check = User.objects.filter(username=number).exists()
        email_check = User.objects.filter(email=email).exists()


        if number_check == True:
            messages.error(request, ' Your Number is Already Exists.')
            return redirect('/signup')


        if email_check == True:
            messages.error(request, ' Your Email is Already Exists.')
            return redirect('/signup')


        if len(number) != 10:
            messages.error(request, ' Numbers should be 10 digit.')
            return redirect('/signup')

        elif password != confirmpassword:
            messages.error(request, ' Password and Confirm Password Did not match please try agian ')
            return redirect('/signup')

        else:
            user = User.objects.create_user(username=number, email=email, password=confirmpassword)
            user.first_name = fname
            user.last_name = lname
            user.is_staff  = True
            user.save()
            messages.success(request, 'Your Account Successfully Create ')
            return redirect('/login')
    return render(request, 'auth/signup.html', {})

