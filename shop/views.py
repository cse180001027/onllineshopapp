from   django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("<h1>h1 hi </h1>")