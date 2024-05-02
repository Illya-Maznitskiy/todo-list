from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "todo_app/index.html")


def home(request):
    return None
