from django.contrib import admin

from todoapp.models import Category, Todo
# Register your models here.

admin.site.register(Category)
admin.site.register(Todo)