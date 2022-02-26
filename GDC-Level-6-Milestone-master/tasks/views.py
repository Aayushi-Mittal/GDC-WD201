# Add all your views here
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms import ModelForm, ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.models import Task


class AuthorizedTaskManager(LoginRequiredMixin):
    def get_queryset(self):
        tasks = Task.objects.filter(deleted=False, user=self.request.user)


class UserLoginView(LoginView):
    template_name = "user_login.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "user_signup.html"
    success_url = "/user/login"


def session_storage_view(request):
    total_views = request.session.get("total_views", 0)
    request.session["total_views"] = total_views + 1
    return HttpResponse(
        f"total views is {total_views} and the user is {request.user} and the user is {request.user.is_authenticated}"
    )

class GenericTaskCompleteView(UpdateView):
    model = Task
    success_url = "/all-tasks"

class GenericTaskDeleteView(DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = "/all-tasks"


class GenericTaskDetailView(AuthorizedTaskManager, DetailView):
    model = Task
    template_name = "task_details.html"


class TaskCreateForm(ModelForm):
    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise ValidationError("Title too short.")
        return title

    class Meta:
        model = Task
        fields = ["title", "description", "completed"]


class GenericTaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "task_update.html"
    success_url = "/all-tasks"


# Passed form to view
class GenericTaskCreateView(CreateView):
    form_class = TaskCreateForm
    template_name = "task_create.html"
    success_url = "/tasks"

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CreateTaskView(View):
    def get(self, request):
        return render(request, "task_create.html")

    def post(self, request):
        task_value = request.POST.get("task")
        task_obj = Task(title=task_value)
        task_obj.save()
        return HttpResponseRedirect("/all-tasks")


class GenericTaskView(ListView, LoginRequiredMixin):

    queryset = Task.objects.filter(completed=False, deleted=False)
    template_name = "tasks.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        search_term = self.request.GET.get("search")
        tasks = Task.objects.filter(completed=False, deleted=False, user=self.request.user)
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

class GenericAllTaskView(LoginRequiredMixin, ListView):
    queryset = Task.objects.filter(deleted=False)
    template_name = "all_tasks.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(deleted=False, user=self.request.user)


class GenericCompletedTaskView(LoginRequiredMixin, ListView):
    queryset = Task.objects.filter(completed=True, deleted=False)
    template_name = "completed_tasks.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(
            completed=True, deleted=False, user=self.request.user
        )

# def add_task_view(request):
#     task_value = request.GET.get("task")
#     task_obj = Task(title=task_value)
#     task_obj.save()
#     return HttpResponseRedirect("/tasks")


# def delete_task_view(request, index):
#     Task.objects.filter(id=index).update(deleted=True)
#     return HttpResponseRedirect("/tasks")


# def complete_task_view(request, index):
#     Task.objects.filter(id=index).update(completed=True)
#     return HttpResponseRedirect("/tasks")
