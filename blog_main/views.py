from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from .forms import Registration_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_post = Blog.objects.filter(is_featured=True, status='Publish').order_by("updated_at")
    posts = Blog.objects.filter(is_featured=False, status='Publish')
    categories = Category.objects.all()  # include categories for navbar

    context = {
        'featured_post': featured_post,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'home.html', context)


def about(request):
    title = 'About us Page',
    content = 'This is the about page of Blogify. We are new in this field and we are make this project only for development purpose and if you like to write blogs and sharing your video on social media platform so you like this.',
    
    context ={
        'title': title,
        'content': content
    }

    return render(request, 'about_us.html', context)


def contact(request):
    title = "Contact page Blogify",
    content = "This is contact page"

    context = {
        'title': title,
        'content': content
    }

    return render(request, 'contact_us.html', context)


def register(request):
    if request.method == "POST":
        form = Registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            pass
    else:
        form = Registration_form()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('login')