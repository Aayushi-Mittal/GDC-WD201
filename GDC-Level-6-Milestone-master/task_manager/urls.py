from django.contrib import admin
from django.urls import path

# from tasks import views

from tasks.views import add_task_view, delete_task_view, GenericTaskView;

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("all_tasks/", views.all_tasks_view),
    path("tasks/", GenericTaskView.as_view()),
    # path("completed_tasks/", views.completed_tasks_view),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    # path("complete_task/<int:index>/", views.complete_task_view),
]