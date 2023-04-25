from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre
from django.db.models import Q

def homepage(request):
    context = {
        
        'movies': Movie.objects.all(),
    }
    return render(request, 'homepage.html', context)
    #return HttpResponse("ahoj")
def movies(request):
    movie_querystring = Movie.objects.all

    genre = request.GET.get('genre')

    if genre:
        movie_querystring = movie_querystring.filter(genres__name=genre)

    search = request.GET.get('search')

    if search:
        movie_querystring = movie_querystring.filter(
            Q(name__icontains=search)|(description__icontains=search)
            )

    context = {
        'movies': movie_querystring,
        'genres': Genre.objects.all().order_by('name'),
        'genre': genre,
        'search': search,
    }
    return render(request, 'movies.html', context)

def movie(request, id):
    context = {
        
        'movies': Movie.objects.get(id=id),
    }
    return render(request, 'movie.html', context)

def directors(request):
    context = {
        
        'movies': Movie.objects.all(),
    }
    return render(request, 'directors.html', context)

def director(request, id):
    context = {
        
        'movies': Movie.objects.get(id=id),
    }
    return render(request, 'director.html', context)

def actors(request, id):
    context = {
        
        'movies': Movie.objects.all
    }
    return render(request, 'director.html', context)

def actor(request, id):
    context = {
        
        'movies': Movie.objects.get(id=id),
    }
    return render(request, 'director.html', context)
