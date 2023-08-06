from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks' : tasks
    }
    return render(request, 'todoapp_app/index.html', context)

def display_task(request, task_id):
    pass

def save_task(request):
    if request.method == "POST":
        task_name = request.POST['task_name']
        task = Task(name=task_name, status=1)
        task.save()
        return redirect('index')
    else:
        return redirect('index')
    
def mark_complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.finished = True
    task.save()
    return redirect('index')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('index')

from django.shortcuts import render, redirect
from .models import Task

def edit_task_view(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('index')  # Or display an error page if the task doesn't exist

    if request.method == 'POST':
        pass
    else:
        pass

    return render(request, 'edit_task.html', {'task': task})

