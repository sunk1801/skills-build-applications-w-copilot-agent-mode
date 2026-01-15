
import uuid
from django.db import models

def uuid_str():
    return str(uuid.uuid4())

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid_str, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid_str, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid_str, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid_str, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(User, related_name='suggested_workouts', blank=True)

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid_str, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    total_points = models.IntegerField(default=0)
