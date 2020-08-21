from rest_framework.routers import SimpleRouter
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import *

router = SimpleRouter()
router.register("profiles", ProfileViewSet)
router.register(r"movies", MovieViewSet)
router.register("haikus", HaikuViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
  url(r'^login/', login),
  url(r'^register/', register),
  url(r'^jwt-auth/', obtain_jwt_token),
]
urlpatterns += router.urls

app_name = 'api'