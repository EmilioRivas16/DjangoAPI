from .models import *
from rest_framework import serializers

class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActorName
        fields = ['name']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'ranking']

class MovieCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieCategories
        fields = ['name']