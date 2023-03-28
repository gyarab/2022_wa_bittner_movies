from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def homepage(request):
    context = {
        
        'movies': Movie.objects.all(),
    }
    return render(request, 'main.html', context)
    #return HttpResponse("ahoj")
