from django.db import models

# Create your models here.
class Movie(models.Model):
    md_id = models.CharField(unique=True, max_length=50)
    title = models.CharField(max_length=200)
    overview = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    poster_url = models.URLField()
    
    