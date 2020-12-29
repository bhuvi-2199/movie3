from django.db import models
import json
from rest_framework import serializers

class Movie(models.Model):

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    year = models.IntegerField()

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'year': self.year
        }

    def __str__(self):
        return str(self.to_dict())


class MovieSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=200)
    director = serializers.CharField(max_length=200)
    year = serializers.IntegerField()

  

class User(models.Model):

    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    my_movies = models.ManyToManyField(Movie)
    
    def to_dict(self):

        return {
            'id': self.id,
            'name': self.name,
            'username': self.username
        }

    def __str__(self):
        return str(self.to_dict())

class UserSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    #password = serializers.CharField(max_length=200)



    

