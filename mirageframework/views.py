from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from miragecore.core.types import *

class CURDView(APIView):
    """
    View to create CRUD interface for general API resource group.

    * Requires token authentication.
    * Only authenticated users are able to access this view.
    """

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
