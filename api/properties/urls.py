from django.conf.urls import include, url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from properties.views import Props

urlpatterns = [
    path('props/', Props.as_view(), name="props")
]
