from django.shortcuts import render, redirect
from .models import Category, Todo
# Create your views here.
def index(request):

    if request.method == 'POST':

        if 'delete' in request.POST:           
            todo_id = request.POST['title']
            toso = Todo.objects.get(pk=todo_id)
            toso.delete()

        if 'save' in request.POST:
            content = request.POST['content']
            due_date = request.POST['due_date']
            title = request.POST['title']
            category_id = request.POST['selected_category']
            category = Category.objects.get(id=category_id)
            toso = Todo(title=title,content=content, due_date=due_date, category=category)
            toso.save()

        if 'search' in request.POST:
            task_id = request.POST['title']

    category = Category.objects.all()
    todo = Todo.objects.all()
    TodoApp = "TodoApp"
    
    context = {
     'todo' : todo,
     'catego' : category,
     'title' : TodoApp,
    }
    return render(request, 'index.HTML', context )