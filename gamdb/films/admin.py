from django.contrib import admin

from .models import Movie, Director, Genre

class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'director', 'year', 'genres_display']
    list_display_links = ['name']
    search_fields = ['name', 'description']
    list_filter = ['genres']



class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'birth_year']
    list_display_links = ['name']
    search_fields = ['name', 'birth_year']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Genre, GenreAdmin)