from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

# from tasks import views

from tasks.views import add_task_view, session_storage_view, GenericTaskView, GenericTaskCreateView, GenericTaskUpdateView, GenericTaskDeleteView, GenericTaskDetailView, UserCreateView, UserLoginView;

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", GenericTaskView.as_view()),
    path("create-task/", GenericTaskCreateView.as_view()),
    path("update-task/<pk>/", GenericTaskUpdateView.as_view()),
    path("delete-task/<pk>/", GenericTaskDeleteView.as_view()),
    path("details-task/<pk>/", GenericTaskDetailView.as_view()),
    path("user/signup/", UserCreateView.as_view()),
    path("user/login/", UserLoginView.as_view()),
    path("user/logout/", LogoutView.as_view()),
    path("sessiontest/", session_storage_view),
    path("add-task/", add_task_view),
]