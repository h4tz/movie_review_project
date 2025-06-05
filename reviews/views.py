from django.shortcuts import render , redirect , get_object_or_404
from rest_framework import viewsets
from .models import Review , Movie
from .serializers import ReviewSerializer
from django.contrib.auth.decorators import login_required 
from .models import Movie
from reviews.forms import ReviewForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise serializers.ValidationError('Authentication required to create a review')
        
@login_required 
def review_movie(request, md_id):
    try:
        movie = Movie.objects.get(md_id=md_id)
    except Movie.DoesNotExist:
        messages.error(request, 'movie not found')   
        return render(request, 'core/error_template.html', {'message': 'Movie not found' })
    existing_review = Review.objects.filter(user=request.user, movie=movie).first()
    
    if request.method == 'POST':
        if existing_review:
            form = ReviewForm(request.POST, instance=existing_review)
        else:
            form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            
            try:
                review.save()
                if existing_review:
                    messages.success(request, 'Your review has been updated Successfully')     
                else:
                    messages.success(request, 'Your review has been submitted successfully')
                return redirect('review_detail', md_id=movie.md_id)
            except Exception as e :
                messages.error(request, f'An Error occured while saving your review: {e} ')
                print(f'Error saving review: {e}')
                return render(request, 'core/error_template.html', {'message': f'Error saving reviews: {e} '})
        else:
            messages.error(request, 'Please correct the errors in the form')
    else:
        if existing_review:
            form=ReviewForm(instance=existing_review)
            messages.info(request,'already reviews can edit  tho?')
        else:
            form = ReviewForm()
    context = {
        'movie' : movie,
        'form': form,
        'existing_review': existing_review,
    }
    return render(request, 'reviews/review_form.html', context)

@login_required
def review_detail(request,md_id):
    movie = get_object_or_404(Movie, md_id=md_id)
    review = get_object_or_404(Review, user=request.user, movie=movie)
    
    context = {
        'movie' : movie,
        'review' : review
    }
    return render(request, 'reviews/review_details.html', context)
1
def review_success(request):
    return render(request, 'reviews/review_success.html')

def movie_list_view(request,md_id=None):
    movies = Movie.objects.all()
    query = ''
    context = {
        'movies' : movies,
        'query' : query,
    }
    return render(request, 'core/index.html', context)