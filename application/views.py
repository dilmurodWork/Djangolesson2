from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("<h1>About page</h1>")


def contact(request, pk: str = 'Name'):
    return render(request, 'contact.html', context={'name': pk})
