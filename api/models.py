from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=150)
  bio = models.TextField(max_length=500, blank=True)
  # below to be revised into ImageField with Pillow
  # utilizing https://www.geeksforgeeks.org/python-uploading-images-in-django/
  image = models.URLField(default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
  join_date = models.DateField(auto_now_add=True)

class Movie(models.Model):
  title = models.CharField(max_length=255)
  poster = models.URLField()

class Haiku(models.Model):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  title = models.CharField(max_length=150)
  line_one = models.CharField(max_length=50)
  line_two = models.CharField(max_length=70)
  line_three = models.CharField(max_length=50)
  post_date = models.DateField(auto_now_add=True)

class Comment(models.Model):
  class Stars(models.IntegerChoices):
    1
    2
    3
    4
    5
  haiku = models.ForeignKey(Haiku, on_delete=models.CASCADE)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  rating = models.IntegerField(choices=Stars.choices)
  comment = models.TextField(max_length=500, blank=True)
  post_date = models.DateField(auto_now_add=True)



# From Tutorial, To Be Deleted
class Subscriber(models.Model):
  name = models.CharField("Name", max_length=50)
  age = models.IntegerField("Age")
  email = models.EmailField("Email")

