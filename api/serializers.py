from rest_framework import serializers

from .models import *

# does anything need to be excluded?
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = "__all__"

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

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"