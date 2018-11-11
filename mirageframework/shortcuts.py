from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from miragecore.core.types import *


def create(request: HttpRequest, serializer_class: callable) -> Response:
        """
        Return a status message.
        """

        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def read(request: HttpRequest, serializer_class: callable) -> Response:
    pass

def update(request: HttpRequest, serializer_class: callable) -> Response:
    pass

def delete(request: HttpRequest) -> Response:
    pass
