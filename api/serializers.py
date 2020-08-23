from rest_framework import serializers

from .models import *

# does anything need to be excluded?

# Title & Link classes (for Haikus, Comments)
class TL_MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['title', 'id']


# This as is works best for the create/update route
class HaikuAddSerializer(serializers.ModelSerializer):
  class Meta:
    model = Haiku
    fields = "__all__"

# This works best for Haiku Show routes
class HaikuShowSerializer(serializers.ModelSerializer):
  movie = TL_MovieSerializer(many=False)
  class Meta:
    model = Haiku
    fields = "__all__"

# This is now perfect for the Movie Show page
# May be good enough for Movie List page
class MovieSerializer(serializers.ModelSerializer):
  haikus = HaikuShowSerializer(many=True, read_only=True)
  class Meta:
    model = Movie
    fields = ("title", "poster", "haikus", "id")

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(many=False)
  haikus = HaikuShowSerializer(many=True)
  class Meta:
    model = User
    fields = ["profile", "id", "username", "haikus"]

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"