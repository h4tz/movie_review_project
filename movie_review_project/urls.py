"""
URL configuration for movie_review_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from core.views import search_movies , select_movie
from reviews.views import ReviewViewSet , review_movie, review_success , review_detail , movie_list_view
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'reviews', ReviewViewSet )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search-movies/', search_movies, name = 'search_movies'),
    path('api/', include(router.urls)),
    path('select-movie/<str:md_id>/', select_movie, name='select_movie'),
    path('review-movie/<str:md_id>/', review_movie, name='review_movie'),
    path('review-detail/<str:md_id>/', review_detail, name='review_detail'),
    path('review-success/', review_success, name='review_success'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('movie/<str:md_id>/', movie_list_view , name = 'movie_detail' ),
    
]
