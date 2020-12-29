from django.urls import path 
from . import views 

urlpatterns = [
    path('all-movies/', views.Movielist.as_view(), name='all_movies'),
    path('movies-for-username/', views.MoviesForUsername.as_view(), name='movies_for_username'),
    path('add-movie-for-user/', views.AddMovieForUser.as_view(), name='add_movie_for_user')
]