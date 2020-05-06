from django.shortcuts import render, redirect

from .models import Category, Todo
# Create your views here.
def index(request):
    
    if request.method == 'POST':
        
        title   =  request.POST['title']
        content   =  request.POST['content']
        due_date   =  request.POST['due_date']
        category_id = request.POST['selected_category']

        print(request.POST)

        category = Category.objects.get(id=category_id)
        todo = Todo(title=title, content=content, due_date=due_date,category=category)
        todo.save()

        print('New Task Title:'+ title)
        print('New Task Content:'+ content)
        print('New Task date:'+ due_date)
        print('New Task category_id:'+ category.name)

        # redirect('/todos')
        

    categories = Category.objects.all()
    todos =  Todo.objects.all()


    return render(request,'index.html', {'categories':categories,'todo_list':todos })
