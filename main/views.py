from django.shortcuts import render
from django.http import HttpResponse  # Додаємо імпорт


# Create your views here.
def index(request):
    context = {
        "title": "HOME",
        "content": "Главная страница магазина - HOME",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "bool": True,
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
