from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework import permissions

from .serializers import UserSerializer

class HelloView(APIView):

    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
