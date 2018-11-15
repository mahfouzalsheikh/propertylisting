from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_jwt.views import ObtainJSONWebToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/properties/', include('properties.urls')),
    path('docs/', include_docs_urls(title='APIs')),
    path('login/', ObtainJSONWebToken.as_view()),
    path('token-refresh/', refresh_jwt_token),
    path('token-verify/', verify_jwt_token),
]
