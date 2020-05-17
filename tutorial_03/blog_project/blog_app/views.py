from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request, slug=None):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

@login_required
def detail(request, slug=None):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/detail.html', {'post':post})

@login_required
def create(request):
    return render(request, 'blog/create.html', {})

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    return render(response, "registration/signup.html", {"form":form})