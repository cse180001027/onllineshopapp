from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse("<h1>h1 hi </h1>")
