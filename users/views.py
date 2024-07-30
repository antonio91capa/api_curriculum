from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import UserModelSerializer, UserLoginSerializer, UserSignUpSerializer, UserLogoutSerializer
from .models import User

# User View Set
class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Logiin del usuario
    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            "user": UserModelSerializer(user).data, 
            "access_token": token
        }

        return Response(data, status=status.HTTP_201_CREATED)

    # Registro del usuario
    @action(detail=False, methods=["post"])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            data = UserModelSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            print(serializer.error_messages)
            return Response({'messages': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
          