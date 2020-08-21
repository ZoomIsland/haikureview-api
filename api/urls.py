from django.conf.urls import url

from .views import HelloWorldView, SubscriberView

urlpatterns = [
    url(r'^hello', HelloWorldView.as_view(), name="hello_world"),
    url(r'^subscriber', SubscriberView.as_view(), name="subscriber")
]

app_name = 'api'