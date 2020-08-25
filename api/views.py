from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.settings import api_settings

from .models import *
from .serializers import *

@api_view(["POST"])
def register(request):
  username = request.data.get("username")
  email = request.data.get("email")
  password = request.data.get("password")
  # what validation should be added here?
  user = User.objects.create_user(username, email, password)
  user.save();
  profile = Profile(user=user, display_name=user.username)
  profile.save();
  # and then create/send the JWT Token
  jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
  jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
  payload = jwt_payload_handler(user)
  token = jwt_encode_handler(payload)
  return Response({"token": token})

@api_view(["POST"])
def login(request):
  username = request.data.get("username")
  password = request.data.get("password")

  user = authenticate(username=username, password=password)
  if not user:
    return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)
  jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
  jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
  payload = jwt_payload_handler(user)
  token = jwt_encode_handler(payload)
  return Response({"token": token})

class ProfileViewSet(ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  # permission_classes = (IsAuthenticatedOrReadOnly)

class UpdateProfileViewSet(ModelViewSet):
  serializer_class = UpdateProfileSerializer
  queryset = Profile.objects.all()
  # permission_classes = (IsAuthenticatedOrReadOnly)

class MovieViewSet(ModelViewSet):
  serializer_class = MovieSerializer
  queryset = Movie.objects.all()
  # Consider: Since a movie is only instantiated prior to commenting, where does it fall? What does it need?
  # permission_classes = (IsAuthenticatedOrReadOnly)

class HaikuAddViewSet(ModelViewSet):
  serializer_class = HaikuAddSerializer
  queryset = Haiku.objects.all()
  # How to handle that Users should only be able to delete/update their OWN haikus?
  # permission_classes = (IsAuthenticatedOrReadOnly)

class HaikuShowViewSet(ModelViewSet):
  serializer_class = HaikuShowSerializer
  queryset = Haiku.objects.all()
  # Don't forget to restrict permissions

class CommentViewSet(ModelViewSet):
  serializer_class = HaikuWithCommentsSerializer
  queryset = Haiku.objects.all()
  # How to handle that Users should only be able to delete/update their OWN haikus?
  # permission_classes = (IsAuthenticatedOrReadOnly)

class NewCommentViewSet(ModelViewSet):
  serializer_class = CommentSerializer
  queryset = Comment.objects.all()

# Backend API creation instantiated by following this tutorial:
# See http://polyglot.ninja/django-rest-framework-getting-started/