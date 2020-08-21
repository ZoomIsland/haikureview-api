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
  class Meta:
    model = Haiku
    fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"


# Below To be Deleted (Tutorial)
class HelloWorldSerializer(serializers.Serializer):
  name = serializers.CharField(required=True, max_length=6)
  age = serializers.IntegerField(required=False, min_value=10, default=10)

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"