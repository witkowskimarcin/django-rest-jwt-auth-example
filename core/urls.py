"""jwt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    path('api-token-refresh/', refresh_jwt_token, name='api_token_auth_refresh'),
    path('api-token-verify/', verify_jwt_token, name='api_token_auth_verify'),
    path('users/register/', views.CreateUserView.as_view(), name="registration"),
]
