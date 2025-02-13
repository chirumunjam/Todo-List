from django.shortcuts import render,redirect
from .models import Todo,History

# Create your views here.

def home(request):
    if request.method == 'POST':
        a = request.POST.get('task')
        b = request.POST.get('description')
        a = Todo.objects.create(task=a, description=b)
    return render(request, 'home.html')

def todolist(request):
    data = Todo.objects.all()
    context = {'data':data}
    return render(request,'todolist.html',context)


def single(request, id):
    todo = Todo.objects.get(id=id)
    context = {'todo': todo}
    if request.method == 'POST':
        a = History.objects.create(task=todo.task, description=todo.description)
        todo.delete()
        return redirect('todolist')
    return render(request, 'single.html', context)

def history(request):
    deleted = History.objects.all()
    context = {'deleted': deleted}
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        remove = History.objects.get(id=task_id)
        remove.delete()
        return redirect('history')
    return render(request, 'history.html', context)

def contact(request):
    return render(request, 'contact.html')

def edit(request, id):
    todo = Todo.objects.get(id=id)
    context = {'todo':todo}
    if request.method == 'POST':
        todo.task=request.POST.get('task')
        todo.description=request.POST.get('description')
        todo.save()
        return redirect('todolist')
    return render(request, 'edit.html', context)
