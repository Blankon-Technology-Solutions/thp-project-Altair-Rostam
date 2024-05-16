from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .api.serializers import TodoListSerializer
from .models import Todo


@login_required
def TodoView(request):
    todos = Todo.objects.filter(user=request.user)
    serializer = TodoListSerializer(todos, many=True)

    return render(request, "todo.html", {"todos": serializer.data, "user": request.user})


@login_required
def ProfileView(request):
    return render(request, "profile.html")
