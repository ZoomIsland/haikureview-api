from rest_framework.routers import SimpleRouter
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import SubscriberViewSet, login

router = SimpleRouter()
router.register("subscribers", SubscriberViewSet)

urlpatterns = [
  url(r'^login/', login),
  url(r'^jwt-auth/', obtain_jwt_token),
]
urlpatterns += router.urls

app_name = 'api'