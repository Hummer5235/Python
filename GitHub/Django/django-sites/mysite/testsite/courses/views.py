from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *



menu = ['О сайте', 'Войти', 'Добавить статью']


def index(request):
    # return HttpResponse('<h1>Главная страница</h1>')
    # return render(request, 'courses/index_old.html', {'menu':menu, 'title':'Главная страница'})
    posts = Courses.objects.all()
    return render(request,'courses/index.html', {'menu':menu, 'title':'Главная страница','posts': posts})

def about(request):
    # return HttpResponse('<h1>Главная страница</h1>')
    return render(request, 'courses/about.html', {'title':'О Сайте'})

def help(request):
    # return HttpResponse('<h1>Главная страница</h1>')
    return render(request, 'courses/help.html', {'title':'Поддержка'})


def courses(request, item = None):

    if request.GET:
        print(request.GET)

    try:
        if int(item) < 0:
            raise Http404
    except ValueError:
        pass

    if item.lower() == 'home':
        return redirect('home')

    return HttpResponse(f'<h1>Страница с курсами по {item}</h1>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')




