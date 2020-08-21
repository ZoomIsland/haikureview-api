from rest_framework import serializers

from .models import Subscriber

class HelloWorldSerializer(serializers.Serializer):
  name = serializers.CharField(required=True, max_length=6)
  age = serializers.IntegerField(required=False, min_value=10, default=10)

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"