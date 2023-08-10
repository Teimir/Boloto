from django.shortcuts import render, redirect
from django.utils import timezone

from .models import New, Post
from .forms import NewForm, LoginForm, SignupForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import QueryDict

def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)

@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        form.data = QueryDict('csrfmiddlewaretoken='+form.data.__getitem__('csrfmiddlewaretoken')+'&title='+form.data.__getitem__('title')+'&text='+form.data.__getitem__('text')+'&author='+str(request.user.id), mutable=True)
        if form.is_valid():
            form.save()
            return redirect("boloto")
        else:
            error = "Отсутствует заголовок или текст поста"
    form = NewForm()

    data = {
        'form': form,
        'error': error,
        'title' : "Что cквакнуло!?"
    }

    return render(request, 'blog/create_post.html', data)


def loginView(request):
    error = ''
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("boloto")
        else:
            error = "Incorrect username or password"
        
    form = LoginForm()
    data = {
        'form': form,
        'error': error,
        'title' :"Войди в аккаунт"
    }

    return render(request, 'blog/login.html', data)

def SignupView(request):
    error = ''
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = User.objects.create_user(username=username, password=password, email=email)
        if user is not None:
            login(request, user)
            return redirect("boloto")
        else:
            error = "Incorrect username or password"
        
    form = SignupForm()
    data = {
        'form': form,
        'error': error,
        'title' :"Создай аккаунт"
    }

    return render(request, 'blog/singup.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страничка про Болото'})

@login_required(login_url='login')
def profileView (request):
    return render(request, 'blog/main.html', {'title': 'Профиль'})

def boloto(request):
    News = Post.objects.all()
    News = list(reversed(News))
    data = {
        'news': News,
        'title': 'Главная страница'
    }
    return render(request, 'blog/boloto.html', data)


