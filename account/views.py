from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from . import models

# Create your views here.

@api_view(["POST"])
def logout_view(request):
    request.user.auth_token.delete()
    request.user.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(["POST"])
def register_view(request):
    serializer = RegistrationSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data["response"] = "Registration Successfull"
        data["email"] = account.email
        data["username"] = account.username

        token = Token.objects.get(user=account)
        data['token'] = token.key

    else:
        data = serializer.errors

    return Response(data, status=status.HTTP_201_CREATED)

