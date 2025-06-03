from django.shortcuts import render , redirect
import requests
from .models import Movie
from django.urls import reverse

def search_movies(request):
    query = request.GET.get('q', '')
    movies = []
    if query :
        
        url = "https://online-movie-database.p.rapidapi.com/auto-complete"
        querystring = {"q": query}
        headers = {
            "x-rapidapi-key": "fab6a4e011mshea3eaa6fe3d0a19p10ced2jsn7f87f24b1823",
            "x-rapidapi-host": "online-movie-database.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring).json()
        movies = response.get('results', [])
        print(response)
        
        if 'd' in response and isinstance(response['d'], list):
            for item in response['d']:
                if item.get('q') in [
                    'feature', 'TV series'
                ]:
                    movies.append(
                        {
                            'md_id' : item.get('id'),
                            'title' : item.get('l'),
                            'release_date' : item.get('y'),
                            'overview' : item.get('s', 'No overview available'),
                        }
                    )
        
    else :
        movies = []
    return render(request, 'core/index.html', {'movies': movies, 'query': query})

def select_movie(request, md_id):
    if not Movie.objects.filter(md_id=md_id).exists():
        print(f"Movie with IMDb ID {md_id} not found in local DB. Fetching from RapidAPI...")
        
        #fetch data
        url = "https://online-movie-database.p.rapidapi.com/title/v2/get-overview"
        querystring = {"tconst": md_id, "country": "US", "language": "en-US"}
    
        rapidapi_key = 'fab6a4e011mshea3eaa6fe3d0a19p10ced2jsn7f87f24b1823' # Make sure this matches your .env variable name
        rapidapi_host = "online-movie-database.p.rapidapi.com"

        headers = {
            "x-rapidapi-key": rapidapi_key,
            "x-rapidapi-host": rapidapi_host
        }
    
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status()
            movie_data = response.json()
        
            title = movie_data.get('titleText',{}).get('text', 'N/A')
            overview = movie_data.get('plot',{}).get('plotText',{}).get('plainText','No overwview')
        
            # date components as YYYY-MM-DD
            release_date_obj = movie_data.get('releaseDate',{})
            release_date = None
            if release_date_obj :
                try:
                    year = release_date_obj.get('year')
                    month = release_date_obj.get('month')
                    day = release_date_obj.get('day')
                    if year and month and day :
                        release_date = f'{year:04d}-{month:02d}-{day:02d}'
                except (TypeError, ValueError):
                    print(f'Warning: could not parse release date for {md_id} ')
                    release_date = None 
            Movie.objects.create(
                md_id=md_id,
                title=title,
                overview=overview,
                release_date=release_date,
                )
            print(f"Successfully saved movie '{title}' ({md_id}) to local DB.")
    
        except requests.exceptions.RequestException as e:
            print(f'Error detching movies details from rapid api for {md_id}: {e}')
            return render(request, 'core/error_template.html', {'message', f'couldnot fetch movie detials: {e}'})
        except KeyError as e:
            print(f"Error parsing RapidAPI response for {md_id}: Missing key {e}. Response: {movie_data}")
            return render(request, 'core/error_template.html', {'message': f"Invalid movie data received: {e}"})
        except Exception as e:
            print(f"An unexpected error occurred for {md_id}: {e}")
            return render(request, 'core/error_template.html', {'message': f"An unexpected error occurred: {e}"})
    else : 
        print(f"Movie with IMDb ID {md_id} already exists in local DB.")
        
    return redirect(reverse('review_movie' , args=[md_id]))     

