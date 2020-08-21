from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

# auth
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import HelloWorldSerializer, SubscriberSerializer
# port above down below here (as needed) for finalized views
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings

from .models import *


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

  # see Login below





# Below To Be Deleted (Tutorial)
#auth
@api_view(["POST"])
def login(request):
  username = request.data.get("username")
  password = request.data.get("password")

  user = authenticate(username=username, password=password)
  if not user:
    return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

  token, _ = Token.objects.get_or_create(user=user)
  return Response({"token": token.key})

# You can also use functions with a decorator (api_view)
# See http://polyglot.ninja/django-rest-framework-getting-started/
# More on API View: https://www.django-rest-framework.org/api-guide/views/#function-based-views
class HelloWorldView(APIView):
  def get(self, request):
    return Response({"message": "Hello World!"})
    # this works!
  
  def post(self, request):
    serializer = HelloWorldSerializer(data=request.data)
    if serializer.is_valid():
      valid_data = serializer.data

      name = valid_data.get("name")
      age = valid_data.get("age")

      return Response({"message": "Hello {}, you're {} years old".format(name, age)})
    else:
      return Response({"errors": serializer.errors})

# class SubscriberView(APIView):
#   def get(self, request):
#     all_subscribers = Subscriber.objects.all()
#     serialized_subscribers = SubscriberSerializer(all_subscribers, many=True)
#     return Response(serialized_subscribers.data)
#   def post(self, request):
#     serializer = SubscriberSerializer(data=request.data)
#     if serializer.is_valid():
#       subscriber_instance = Subscriber.objects.create(**serializer.data)
#       return Response({"message": "Created subscriber {}".format(subscriber_instance.id)})
#     else:
#       return Response({"errors": serializer.errors})
class SubscriberView(ListCreateAPIView):
    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    # Uhhhhhhhh


class SubscriberViewSet(ModelViewSet):
  serializer_class = SubscriberSerializer
  queryset = Subscriber.objects.all()
  permission_classes = (IsAuthenticatedOrReadOnly,)