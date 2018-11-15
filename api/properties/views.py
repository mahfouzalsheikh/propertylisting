from django.shortcuts import render
from rest_framework import generics, status, views
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from properties.serializers import CreatePropSerializer, PropSerializer
from utils.models import StandardResultsSetPagination
from django.http import HttpResponse
from properties.models import Prop


class Props(generics.ListAPIView):
    """
    get:
    Return a list of all the properties.

    post:
    Create a new property.
    """
    pagination_class = StandardResultsSetPagination
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    queryset = Prop.objects.all()
    serializer_class = CreatePropSerializer

    def get_queryset(self):
        props = Prop.objects.all()
        return props

    def list(self, request, *args, **kwargs):
        self.serializer_class = PropSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)


        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = CreatePropSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            prop = serializer.save()
            return Response(PropSerializer(prop).data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    