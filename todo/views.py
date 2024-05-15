from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .api.serializers import TodoListSerializer
from .models import Todo


@login_required
def TodoView(request):
    todos = Todo.objects.all()
    serializer = TodoListSerializer(todos, many=True)

    return render(request, "todo.html", {"todos": serializer.data})
