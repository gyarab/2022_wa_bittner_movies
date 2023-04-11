from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def homepage(request):
    context = {
        
        'movies': Movie.objects.all(),
    }
    return render(request, 'homepage.html', context)
    #return HttpResponse("ahoj")
def movies(request):
    context = {
        
        'movies': Movie.objects.all(),
    }
    return render(request, 'movies.html', context)

def directors(request):
    context = {
        
        'movies': Movie.objects.all(),
    }
    return render(request, 'directors.html', context)

