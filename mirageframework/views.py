from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from miragecore.core.types import *


def CREATE(request: HttpRequest, serializer_class: callable) -> Response:
        """
        Return a status message.
        """

        serializer = getattr(serializer_class, "SELIALIZER_CLASS")(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CURDView(APIView):
    """
    View to create CRUD interface for general API resource group.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
