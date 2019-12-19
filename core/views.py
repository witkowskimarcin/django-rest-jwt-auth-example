from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.forms import UserCreationForm

class HelloView(APIView):

    permission_classes = (IsAuthenticated,)  

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
