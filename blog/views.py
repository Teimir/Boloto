from django.core import serializers
from django.shortcuts import render, redirect
from .models import New, Newa
from .forms import NewForm


def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("boloto")
        else:
            error = "Не верная форма" + str(form)
    form = NewForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'blog/create_post.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'Страничка про Болото'})


def boloto(request):
    News = Newa.objects.all()
    News = list(reversed(News))
    print(News)
    data = {
        'news': News,
        'title': 'Главная страница'
    }
    return render(request, 'blog/boloto.html', data)