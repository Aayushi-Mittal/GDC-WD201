# Add all your views here
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.forms import ModelForm, ValidationError    

from tasks.models import Task


# def all_tasks_view(request):
#     return render(
#         request,
#         "all_tasks.html",
#         {
#             "tasks": Task.objects.filter(deleted=False).filter(completed=False),
#             "completed_tasks": Task.objects.filter(deleted=False).filter(completed=True),
#         },
#     )

# def completed_tasks_view(request):
#     return render(request, "completed_tasks.html", {"completed_tasks": Task.objects.filter(deleted=False).filter(completed=True)})

# Form
class TaskCreateForm(ModelForm):
    
    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise ValidationError("Title too short.")
        return title.upper()

    class Meta:    
        model = Task
        fields = ["title", "description", "completed"]

class GenericTaskUpdateView(UpdateView):
    model=Task
    form_class=TaskCreateForm
    template_name="task_update.html"
    success_url="/tasks"

# Passed form to view
class GenericTaskCreateView(CreateView):
    form_class = TaskCreateForm
    template_name = "task_create.html"
    success_url = "/tasks"


class CreateTaskView(View):
    def get(self, request):
        return render(request, "task_create.html")

    def post(self, request):
        task_value = request.POST.get("task")
        task_obj = Task(title=task_value)
        task_obj.save()
        return HttpResponseRedirect("/tasks")


class GenericTaskView(ListView):

    queryset = Task.objects.filter(deleted=False)
    template_name = "tasks.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        search_term = self.request.GET.get("search")
        tasks = Task.objects.filter(deleted=False)
        if search_term:
            tasks = tasks.filter(title__icontains=search_term)
        return tasks


class TaskView(View):
    def get(self, request):
        search_term = request.GET.get("search")
        tasks = Task.objects.filter(deleted=False)
        if search_term:
            tasks = tasks.filter(title__icontains=search_term)
        return render(request, "tasks.html", {"tasks": tasks})

    def post(self, request):
        pass


def add_task_view(request):
    task_value = request.GET.get("task")
    task_obj = Task(title=task_value)
    task_obj.save()
    return HttpResponseRedirect("/tasks")


def delete_task_view(request, index):
    Task.objects.filter(id=index).update(deleted=True)
    return HttpResponseRedirect("/tasks")


def complete_task_view(request, index):
    Task.objects.filter(id=index).update(completed=True)
    return HttpResponseRedirect("/tasks")
