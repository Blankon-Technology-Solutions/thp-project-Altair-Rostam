from django.shortcuts import render


def TodoView(request):
    return render(request, "todo.html")
