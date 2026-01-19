from django.shortcuts import render
from .models import Project, Task, Comment

def dashboard(request):
    projects = Project.objects.all()
    tasks = Task.objects.all()
    comments = Comment.objects.all()
    
    context = {
        'projects': projects,
        'tasks': tasks,
        'comments': comments,
    }
    return render(request, 'pm_core/dashboard.html', context)