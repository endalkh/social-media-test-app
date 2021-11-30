from rest_framework import serializers, status
from authentication import models as authentication
from django.contrib.auth import authenticate
from utitilities import exception_handler
from rest_framework.authtoken.models import Token


class UserLoginSerializer(serializers.ModelSerializer):
    """serializer for user login"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = authentication.User
        fields = ("email", "password")

    def create(self, validated_data):
        print("hello")

        user = authenticate(
            email=validated_data.get("email"),
            password=validated_data.get("password"),
        )
        if not user:
            raise exception_handler.CustomValidation(
                "detail", "Invalid Credentials", status.HTTP_401_UNAUTHORIZED
            )
        token, _created = Token.objects.get_or_create(user=user)
        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "token": token.key,
        }


class UserSignupSerializer(serializers.ModelSerializer):
    """serializer for user Signup"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = authentication.User
        fields = (
            "email",
            "password",
            "name",
        )

    def create(self, validated_data):
        user = authentication.User.objects.create_user(
            email=validated_data.get("email"),
            name=validated_data.get("name"),
            password=validated_data.get("password"),
        )
        token, _created = Token.objects.get_or_create(user=user)
        return {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "password": user.password,
            "token": token.key,
        }
