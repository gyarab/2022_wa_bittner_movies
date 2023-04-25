from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    avg_rating = models.FloatField()
    slug = models.SlugField()
    year = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre', blank=True)

    def __str__(self):
        return f"{self.name} ({self.year})"
    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])


class Director(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

class coment(models.Model):
    author = models.CharField(max_length=225)
    text = models.TextField()
    rting = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    birth_year = models.IntegerField(blank=True, null=True)
    photo_url = models.CharField(blank=True, null=True)
    description = models.CharField(blank=True, null=True)

"py -3 -m venv venv"
"django-admin startproject"
"              startapp"


"python manage.py makemigrations            - připraví migrační script"
"python manage.py migrate"

"python manage.py create superuser"
"python manage.py runserver"
"                 dumpdata -format yaml  films>films.yaml"
"                 loaddata films.yaml"
"                          fixtures/* "
" python manage.py   .............   ./manage.py"
"export PITHONIOENCODING=utf-8"
"set                          "

