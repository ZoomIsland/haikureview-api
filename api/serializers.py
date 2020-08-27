from rest_framework import serializers

from .models import *

# does anything need to be excluded?

# Title & Link classes (for Haikus, Comments)
class TL_MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ['title', 'id']

# Used for Profile -> Haikus -> Movies
class FullData_MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = "__all__"

class FullData_HaikuSerializer(serializers.ModelSerializer):
  movie = FullData_MovieSerializer(many=False)
  class Meta:
    model = Haiku
    fields = "__all__"

# This as is works best for the create/update route
class HaikuAddSerializer(serializers.ModelSerializer):
  class Meta:
    model = Haiku
    fields = "__all__"

# This works fine for my User get requests
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = "__all__"

# This is for my Profile only put request
class UpdateProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ("id", "bio", "display_name")

class UserSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(many=False)
  haikus = FullData_HaikuSerializer(many=True)
  class Meta:
    model = User
    fields = ["profile", "id", "username", "haikus"]



# Comment Update
class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"

# Comment Show

class UserSerializerIDwProfileName(serializers.ModelSerializer):
  profile = ProfileSerializer(many=False)
  class Meta:
    model = User
    fields = ["profile", "id"]

class CommentWUserSerializer(serializers.ModelSerializer):
  user = UserSerializerIDwProfileName(many=False)
  class Meta:
    model = Comment
    fields = ["rating", "comment", "post_date", "user", "id"]

class HaikuWithCommentsSerializer(serializers.ModelSerializer):
  comments = CommentWUserSerializer(many=True)
  class Meta:
    model = Haiku
    fields = ["id", "comments"]

# This works best for Haiku Show routes
# user with Profile info only
class UserNameWIdSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(many=False)
  class Meta:
    model = User
    fields = ["profile", "id"]

class HaikuShowSerializer(serializers.ModelSerializer):
  movie = TL_MovieSerializer(many=False)
  comments = CommentWUserSerializer(many=True)
  user = UserNameWIdSerializer(many=False)
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