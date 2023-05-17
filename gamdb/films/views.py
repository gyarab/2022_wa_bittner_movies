from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre, Comment, Actor, Director
from django.db.models import Q
from .forms import CommentForm

def homepage(request):
    context = {
        
        "movies": Movie.objects.all(),
        "actors": Actor.objects.all(),
        "directors": Director.objects.all(),
        "genres": Genre.objects.all(),
    }
    return render(request, 'homepage.html', context)
    #return HttpResponse("ahoj")

def movies(request):
    movies_queryset = Movie.objects.all()

    genre = request.GET.get('genre')

    if genre:
        movies_queryset = movies_queryset.filter(genres__name=genre)

    search = request.GET.get('search')

    if search:
        movies_queryset = movies_queryset.filter(Q(name__icontains=search)|Q(description__icontains=search))

    context = {
        'movies': movies_queryset,
        'genres': Genre.objects.all().order_by('name'),
        'genre': genre,
        'search': search,
    }
    return render(request, 'movies.html', context)

def movie(request, id):
    m = Movie.objects.get(id=id)
    form = CommentForm()

    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment (movie=m, 
                        author=form.cleaned_data['author'], 
                        text = form.cleaned_data['text'], 
                        rating = form.cleaned_data['rating']
                        )
            if not c.author:
                c.author = 'anonym'
            c.save()
            form = CommentForm()
    context = {
        'form':form,
        'movie': m,
        'comments': Comment.objects.filter(movie=m).order_by('-created_at')
    }
    return render(request, 'movie.html', context)

def directors(request):
    context = {
        
        'directors': Director.objects.all(),
    }
    return render(request, 'directors.html', context)

def director(request, id):
    context = {
        
        'director': Director.objects.get(id=id),
    }
    return render(request, 'director.html', context)

def actors(request, id):
    context = {
        
        'actors': Actor.objects.all
    }
    return render(request, 'actors.html', context)

def actor(request, id):
    context = {
        
        'actor': Actor.objects.get(id=id),
    }
    return render(request, 'actor.html', context)
