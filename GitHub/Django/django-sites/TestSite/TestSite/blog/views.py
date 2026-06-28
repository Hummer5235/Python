from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse('<h1>Главная страница<h1/>')



def missed_cases(request, day_id):
    if request.GET:
        print(request.GET)
    if request.POST:
        print(request.POST)

    return HttpResponse(f'<h1>Пропущенные дела {day_id}<h1/>')

def pageNotFound(request , exception):
    return  HttpResponseNotFound('<h1>Страница не найдена</h1>')


