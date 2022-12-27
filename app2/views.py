from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sri(request):
    return HttpResponse('<h1>This is sri view</h1>')
