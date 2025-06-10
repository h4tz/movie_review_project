from django.db import models
from django.contrib.auth.models import User 
from core.models import Movie

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], help_text='RATE From 1-5')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta : 
        ordering = ['-created_at']
        unique_together = ('user', 'movie')
        
    def __str__(self):
        return F'Review by {self.user.username} for {self.movie.title} - {self.rating} stars {self.movie.md_id} '