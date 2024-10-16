from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import User, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
