from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def getAllProjects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects/projects.html', {
        'projects': projects
    })

def getAllTasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })

def getTaskByTitle(request, taskTitle):
    task = get_object_or_404(Task, title=taskTitle)
    return HttpResponse("<h1>Task Title: %s</h1>" %task.title)

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2) 
        return redirect('/tasks/')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {'form':CreateNewProject()} )
    else:
        Project.objects.create(name=request.POST['name']) 
        return redirect('/projects/') 