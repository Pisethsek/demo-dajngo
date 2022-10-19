from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
    return render(request, 'movies/movies.html', {'movies':['m1','m2']})

def home(request):
    return HttpResponse("Home page")

