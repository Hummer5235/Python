from django.contrib import admin

# Register your models here.
from .models import *

class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','time_create','photo','is_published') # Список отображаемых полей
    list_display_links = ('id', 'title') # Список полей в виде ссылок
    search_fields = ('title','content') # Поля для поиска по записям
    list_editable = ('is_published',)
    list_filter = ('is_published','time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    search_fields = ('name',)


#Регистрация моделей
admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
