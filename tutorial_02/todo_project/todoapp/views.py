from django.shortcuts import render, redirect

from .models import Category, Todo
# Create your views here.
def index(request):
    
    if request.method == 'POST':
        if 'save' in request.POST:
            title   =  request.POST['title']
            content   =  request.POST['content']
            due_date   =  request.POST['due_date']
            category_id = request.POST['selected_category']
            category = Category.objects.get(id=category_id)
            todo = Todo(title=title, content=content, due_date=due_date,category=category)
            todo.save()

            print('New Task Title:'+ title)
            print('New Task Content:'+ content)
            print('New Task date:'+ due_date)
            print('New Task category_id:'+ category.name)


            print(request.POST)
        if 'delete' in request.POST:
            todo_id= request.POST['val']
            dele=Todo.objects.get(id=todo_id)
            dele.delete()

        
        # redirect('/todos')
        

    categories = Category.objects.all()
    todos =  Todo.objects.all()


    return render(request,'index.html', {'categories':categories,'todo_list':todos })
