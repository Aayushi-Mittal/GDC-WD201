from django.contrib import admin
from django.urls import path

# from tasks import views

from tasks.views import add_task_view, delete_task_view, GenericTaskView, GenericTaskCreateView, GenericTaskUpdateView, GenericTaskDeleteView, GenericTaskDetailView;

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", GenericTaskView.as_view()),
    path("create-task/", GenericTaskCreateView.as_view()),
    path("update-task/<pk>/", GenericTaskUpdateView.as_view()),
    path("delete-task/<pk>/", GenericTaskDeleteView.as_view()),
    path("details-task/<pk>/", GenericTaskDetailView.as_view()),
    path("add-task/", add_task_view),
]