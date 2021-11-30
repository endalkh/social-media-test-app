from rest_framework import response, status, views
from authentication import serializers, models as authentication
from rest_framework import generics
from django.contrib.auth import authenticate
from utitilities import exception_handler
from rest_framework.authtoken.models import Token


class SigninAPIView(generics.CreateAPIView):
    """Create a new user in the system"""

    queryset = authentication.User.objects.all()
    serializer_class = serializers.UserLoginSerializer
    permission_classes = ()

    def post(self, request):
        user = authenticate(
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        if not user:
            raise exception_handler.CustomValidation(
                "detail", "Invalid Credentials", status.HTTP_401_UNAUTHORIZED
            )
        token, _created = Token.objects.get_or_create(user=user)
        return response.Response(
            {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "token": token.key,
            }
        )


class SignupAPIView(generics.CreateAPIView):
    """Create a new user in the system"""

    queryset = authentication.User.objects.all()
    serializer_class = serializers.UserSignupSerializer
    permission_classes = ()
