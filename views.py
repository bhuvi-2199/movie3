from django.shortcuts import render

from django.http import HttpResponse
from .models import Movie, User, MovieSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from rest_framework import serializers

class Message:

    def __init__(self,message):
        self.message = message
    
class MessageSerializer(serializers.Serializer): 
    message = serializers.CharField(max_length=200)

class Movielist (APIView):

    def get(self,request):

        movies = [movie for movie in Movie.objects.all()]
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)


class MoviesForUsername (APIView):

    def post(self,request):

        x = request.POST.get('username')
        pwd = request.POST.get('password')

        print(x,pwd)

        try:
            user = User.objects.get(username=x,password=pwd) 
        except:
            message = Message('Invalid credentials')
            serializer = MessageSerializer(message)
            return Response(serializer.data)

        movies = [movie for movie in user.my_movies.all()]
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)


class AddMovieForUser (APIView):

    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        #movie_id = request.POST.get('movie_id')
        movie_name = request.POST.get('movie_name')

        print(username,password,movie_name)

        try:
            user = User.objects.get(username=username,password=password)
        except:
            message = Message('Invalid username or password')
            serializer = MessageSerializer(message)
            return Response(serializer.data)

        try: 
            movie = Movie.objects.get(title=movie_name)
        except:
            message = Message('Movie with given name does not exist')
            serializer = MessageSerializer(message)
            return Response(serializer.data)

        try:
            existing_movie = user.my_movies.get(id=movie.id)
        except:
            existing_movie = None 

        if (existing_movie != None):
            message = Message('Movie with given name already added for the given user')
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        
        user.my_movies.add(movie)
        message = Message('Successfully added movie for user')
        serializer = MessageSerializer(message)
        return Response(serializer.data)
        




'''class Userlist (APIView):

    def get(self,request):

        users = [user for user in User.objects.all()]
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)'''