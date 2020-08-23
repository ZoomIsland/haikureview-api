from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=150)
  bio = models.TextField(max_length=500, blank=True)
  # below to be revised into ImageField with Pillow
  # utilizing https://www.geeksforgeeks.org/python-uploading-images-in-django/
  image = models.URLField(default="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
  join_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.display_name

class Movie(models.Model):
  title = models.CharField(max_length=255)
  poster = models.URLField()

  def __str__(self):
    return self.title

class Haiku(models.Model):
  movie = models.ForeignKey(Movie, related_name='haikus', on_delete=models.CASCADE)
  user = models.ForeignKey(User, related_name='haikus', on_delete=models.CASCADE)
  title = models.CharField(max_length=150)
  line_one = models.CharField(max_length=50)
  line_two = models.CharField(max_length=70)
  line_three = models.CharField(max_length=50)
  post_date = models.DateField(auto_now_add=True)

class Comment(models.Model):
  haiku = models.ForeignKey(Haiku, related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE)
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  comment = models.TextField(max_length=500, blank=True)
  post_date = models.DateField(auto_now_add=True)