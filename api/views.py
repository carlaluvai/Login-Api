# Create your views here.

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """This endpoint allows for viewing users"""
    # parser_classes = (MultiPartParser)

    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all().order_by('date_joined')
