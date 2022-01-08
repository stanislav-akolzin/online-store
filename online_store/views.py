from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth.models import User


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    '''Register new user. Return token when success.'''
    username = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    if username is None or email is None or password is None or password_confirmation is None:
        return Response({'error': 'Please privide all required fields'},
                        status=HTTP_400_BAD_REQUEST)
    find_user = User.objects.filter(username=username.lower())
    if len(find_user) == 1:
        return Response({'status': 'error', 'response': 'Such user already exists'},
                        status=HTTP_400_BAD_REQUEST)
    else:
        if password != password_confirmation:
            return Response({'status': 'error', 'response': 'Failed password confirmation'},
                            status=HTTP_400_BAD_REQUEST)
        else:
            user = User.objects.create(username=username.lower(), email=email)
            user.set_password(str(password))
            user.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'status': 'success', 
                            'response': 'User successfully created', 
                            'access_token': token.key},
                            status=HTTP_200_OK)
    

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    '''Login existing user. Return token when success.'''
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None  or password is None:
        return Response({'error': 'Please privide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid user'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'access_token': token.key},
                    status=HTTP_200_OK)