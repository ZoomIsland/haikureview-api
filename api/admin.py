from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Haiku)
admin.site.register(Comment)