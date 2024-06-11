# this will allow us to run python code for any api whenever it gets called

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from rest_framework.authtoken.models import Token
from authentication.models import User
from django.shortcuts import get_object_or_404
from authentication.serializers import UserSerializer 

@api_view(['POST'])
def login(request): 
    user = get_object_or_404(User, email = request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status = status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user = user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request): 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.create(user = user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication #this allows us to authenticate sessions w a token
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request): 
    return Response("passed for {}".format(request.user.email)) 