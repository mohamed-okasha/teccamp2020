
from django.urls import path , include
from blog_app.views import index, detail, home, create

app_name = 'blog_app'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='new_post'),
    path('<slug:slug>/', detail, name='detail'),
    
]
