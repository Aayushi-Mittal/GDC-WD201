# Add all your views here
from django.shortcuts import render
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
