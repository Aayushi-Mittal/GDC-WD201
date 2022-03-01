from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.models import User

from tasks.models import Task
from tasks.models import STATUS_CHOICES

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, ChoiceFilter


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username"]

class TaskSerializer(ModelSerializer):
    
    # Nested Serializers
    user = UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ["title", "description", "completed", "status", "user"]


class TaskFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains")


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    status = ChoiceFilter(choices=STATUS_CHOICES)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, deleted=False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListAPI(APIView):
    def get(self, request):
        tasks = Task.objects.filter(deleted=False)
        data = TaskSerializer(tasks, many=True).data
        return Response({"tasks": data})
