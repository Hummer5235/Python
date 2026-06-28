from django.contrib import admin
from django.urls import path
from blog.views import *


urlpatterns = [
    path('', index),
    path('missed_cases/<int:day_id>/',missed_cases),
]

