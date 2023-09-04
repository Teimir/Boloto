from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import New, Post, Profile
from .forms import NewForm, LoginForm, SignupForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

def home(request):
    return redirect("boloto")

@login_required(login_url='login')
def create(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
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
        username = request.POST["username"].strip()
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
        username = request.POST["username"].strip()
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
def profile_view(request, username):
    # Получить пользователя по его имени пользователя(username)
    user = get_object_or_404(User, username=username)

    try:
        # Попытка получить профиль пользователя
        profile = user.profile
    except:
        # Если профиль не существует, создайте его
        profile = Profile(user=user)
        profile.save()

    posts = get_user_posts(username)

    context = {
        'user': user,
        'profile': profile,
        'posts': posts
    }
    return render(request, 'blog/profile.html', context)

def get_user_posts(user):
    posts = []
    News = Post.objects.all()
    News = list(reversed(News))
    for i in range(len(News)):
        if str(News[i].author) == user:
            posts.append(News[i])
    return posts


def boloto(request):
    News = Post.objects.all()
    News = list(reversed(News))
    data = {
        'news': News,
        'title': 'Главная страница'
    }
    for i in range(len(News)):
        if News[i].img:
            print(News[i].img.url, "|")

    return render(request, 'blog/boloto.html', data)




