from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import logout

from authentication.models import Profile
from authentication import serializers
from authentication import permissions


class AuthenticationViewSet(viewsets.GenericViewSet):

    queryset = Profile.objects.all()

    @action(
        methods=['POST'],
        detail=False,
        url_path='login',
        url_name='login',
        serializer_class=serializers.LoginSerializer)
    def login_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.login_user()
        return Response({'detail': 'Login Successful'})

    @action(
        methods=['POST'],
        detail=False,
        url_path='register',
        url_name='register',
        serializer_class=serializers.RegisterUserSerializer,
        permission_classes=[permissions.IsNotAuthenticated])
    def register_user(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'User Registeration Successful'})

    @action(
        methods=['GET'],
        detail=False,
        url_path='logout',
        url_name='logout')
    def logout_user(self, request):
        logout(request)
        return Response({'detail': 'Logged Out Successfully'})
