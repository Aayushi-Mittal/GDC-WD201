from django.contrib import admin
from django.urls import path

# from tasks import views

from tasks.views import add_task_view, delete_task_view, GenericTaskView, CreateTaskView;

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", GenericTaskView.as_view()),
    path("create-task/", CreateTaskView.as_view()),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
]