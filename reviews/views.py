from django.shortcuts import render
from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from django.contrib.auth.decorators import login_required 
from .models import Movie
from reviews.forms import ReviewForm

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
        message.error(request, 'movie not found')   
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
            review.movie = movie.title
            
            try:
                review.save()
                if existing_review:
                    messages.success(request, 'Your review has been updated Successfully')
                else:
                    messages.success(request, 'Your review has been submitted successfully')
                return redirect(reverse('review_success'))
            except Exception as e :
                message.error(request, f'An Error occured while saving your review: {e} ')
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
        'movie' = movie,
        'form': form,
        'existing_review': existing_review,
    }
    return render(request, 'reviews/review_form.html', context)
1
def review_success(request):
    return render(request, 'reviews/review_success.html')