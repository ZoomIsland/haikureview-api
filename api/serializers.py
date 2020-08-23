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

class TL_ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ['display_name', 'id']


class HaikuSerializer(serializers.ModelSerializer):
  # user = TL_ProfileSerializer(many=False)
  # movie = TL_MovieSerializer(many=False)
  # user = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
  # movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
  class Meta:
    model = Haiku
    fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"