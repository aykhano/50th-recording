from django.shortcuts import render
from .models import Task

def home_page(request):
    tasks = Task.objects.all()
    context = {"task_list": tasks}
    return render(request, 'home.html', context)

def create_new_tasks(request):
    task = request.POST.get("task_title")
    Task.objects.create(title=task)
    pass
