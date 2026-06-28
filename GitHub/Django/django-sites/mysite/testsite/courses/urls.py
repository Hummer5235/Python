

from  django.urls import path
from .views import *

# Список маршрутов внутри приложения
urlpatterns = [
    path('', index, name = 'home'),
    path('course/<slug:item>/', courses),
    path('about/', about, name = 'about'),
    path('help/', help, name = 'help')
]


