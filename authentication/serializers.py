from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate, login, get_user_model

from authentication.models import Profile


User = get_user_model()


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    def login_user(self):
        email = self.validated_data['email']
        password = self.validated_data['password']
        user = authenticate(username=email, password=password)

        if user is None:
            raise AuthenticationFailed(detail='Authentication details are not right')
        login(request=self.context['request'], user=user)


class RegisterUserSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=200)
    password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})
    confirm_password = serializers.CharField(style={'input_type': 'password', 'placeholder': 'Password'})

    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    allowed_calories_per_day = serializers.IntegerField()

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('This email Already exists')
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('Given Passwords do not match')
        return attrs

    def create(self, validated_data):
        del validated_data['confirm_password']
        return Profile.objects.create(**validated_data)
