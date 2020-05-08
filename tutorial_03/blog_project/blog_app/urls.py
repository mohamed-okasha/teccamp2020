
from django.urls import path
from blog_app.views import index, detail, home

app_name = 'blog_app'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>', detail, name='detial')
]
