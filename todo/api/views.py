from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import Todo
from .serializers import TodoDetailSerializer, TodoListSerializer


class TodoListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Trigger websocket event when a new todo is created
        instance = serializer.save(user=self.request.user)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "todo_updates", {"type": "update_todos", "data": TodoListSerializer(instance).data}
        )


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # Trigger websocket event when a todo is updated
        instance = serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "todo_updates", {"type": "update_todos", "data": TodoDetailSerializer(instance).data}
        )

    def perform_destroy(self, instance):
        # Trigger websocket event when a todo is deleted
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "todo_updates", {"type": "update_todos", "data": {"id": instance.id, "deleted": True}}
        )
        instance.delete()
