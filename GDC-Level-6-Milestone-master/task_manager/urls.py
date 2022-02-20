from django.contrib import admin
from django.urls import path

from tasks.views import add_task_view, delete_task_view, TaskView


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("all_tasks/", all_tasks_view),
    # path("completed_tasks/", completed_tasks_view),
    path("tasks/", TaskView.as_view()),
    path("add-task/", add_task_view),
    path("delete-task/<int:index>/", delete_task_view),
    # path("complete_task/<int:index>/", complete_task_view),
]