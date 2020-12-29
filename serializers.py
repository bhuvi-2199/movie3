from rest_framework import serializers
from rest_framework import Movie
from rest_framework import User

     class MovieSerializer(Serializers.ModelSerializer):
        
        class Meta:
            Model=Movie
            fields= '__all__'
     class UserSerializer(Serializers.ModelSerializer):
        
        class Meta:
            Model=User
            fields= '__all__'
