from django.shortcuts import redirect, render

from .api.serializers import TodoListSerializer
from .models import Todo


def TodoView(request):
    todos = Todo.objects.all()
    serializer = TodoListSerializer(todos, many=True)

    if request.method == "POST":
        newTodo = request.POST["task"]
        todo = Todo.objects.create(content=newTodo)
        todo.save()
        print(request.path)
        return redirect(request.path)

    return render(request, "todo.html", {"todos": serializer.data})
