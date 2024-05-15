from rest_framework import generics

from ..models import Todo
from .serializers import TodoDetailSerializer, TodoListSerializer


class TodoListCreate(generics.ListCreateAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
