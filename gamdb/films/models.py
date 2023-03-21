from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.year})"

"python manage.py makemigrations            - připraví migrační script"
"python manage.py migrate"

"python manage.py create superuser"
"python manage.py runserver"
"                 dumpdata -format yaml  films>films.yaml"
"                 loaddata films.yaml"

" python manage.py   .............   ./manage.py"