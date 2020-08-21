from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import HelloWorldSerializer, SubscriberSerializer
from .models import Subscriber

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