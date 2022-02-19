# Add all your views here
from django.shortcuts import render
from django.http import HttpResponseRedirect

from tasks.models import Task


def all_tasks_view(request):
    return render(
        request,
        "all_tasks.html",
        {
            "tasks": Task.objects.filter(deleted=False).filter(completed=False),
            "completed_tasks": Task.objects.filter(deleted=False).filter(completed=True),
        },
    )


def tasks_view(request):
    search_term = request.GET.get("search")
    tasks = Task.objects.filter(deleted=False).filter(completed=False)
    if search_term:
        tasks = tasks.filter(title__icontains=search_term)
    return render(request, "tasks.html", {"tasks": tasks})


def completed_tasks_view(request):
    return render(request, "completed_tasks.html", {"completed_tasks": Task.objects.filter(deleted=False).filter(completed=True)})


def add_task_view(request):
    task_value = request.GET.get("task")
    task_obj = Task(title=task_value)
    task_obj.save()
    return HttpResponseRedirect("/all_tasks")


def delete_task_view(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/all_tasks")


def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/all_tasks")