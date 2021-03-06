from django.db import models

# Create your models here.

class ActorName(models.Model):
    name = models.CharField(max_length=250) 

class Actor(models.Model):
    name = models.CharField(max_length=250) 

class MovieCategories(models.Model):
    name = models.CharField(max_length=250)

class Movie(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    ranking = models.IntegerField(1)
    category = models.ForeignKey(MovieCategories, on_delete=models.PROTECT)
    actor = models.ManyToManyField(Actor)
    

