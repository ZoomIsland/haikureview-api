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

class HaikuSerializer(serializers.ModelSerializer):
  user = serializers.StringRelatedField(many=False)
  movie = serializers.StringRelatedField(many=False)
  class Meta:
    model = Haiku
    fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"