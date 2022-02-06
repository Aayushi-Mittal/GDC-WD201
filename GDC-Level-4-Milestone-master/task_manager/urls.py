from django.contrib import admin
from django.urls import path

from tasks import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Add all your views here
    path("all_tasks/", views.all_tasks_view),
    path("tasks/", views.tasks_view),
    path("completed_tasks/", views.completed_tasks_view),
]