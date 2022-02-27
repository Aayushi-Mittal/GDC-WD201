# Add all your views here
from django.shortcuts import render
from django.http import HttpResponseRedirect
from tasks import views

# tasks = ["This is my first task"]
# completed_tasks = ["I am done", "second done"]
tasks = []
completed_tasks = []


def all_tasks_view(request):
    return render(
        request,
        "all_tasks.html",
        {
            "tasks": tasks,
            "completed_tasks": completed_tasks,
        },
    )


def tasks_view(request):
    return render(request, "tasks.html", {"tasks": tasks})


def completed_tasks_view(request):
    return render(request, "completed_tasks.html", {"completed_tasks": completed_tasks})

def add_task_view(request):
    task_value = request.GET.get("task")
    if task_value:
        tasks.append(task_value)
    return HttpResponseRedirect("/all_tasks")


def delete_task_view(request, index):
    if index>=1 and index<=len(tasks):
        del tasks[index - 1]
    return HttpResponseRedirect("/all_tasks")


def complete_task_view(request, index):
    if index>=1 and index<=len(tasks):
        completed_tasks.append(tasks.pop(index - 1))
    return HttpResponseRedirect("/all_tasks")