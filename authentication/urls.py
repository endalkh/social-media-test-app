from django.urls import path
from authentication import views

app_name = "authentication"
urlpatterns = [
    path(
        "signup",
        views.SignupAPIView.as_view(),
        name="signup",
    ),
    path(
        "signin",
        views.SigninAPIView.as_view(),
        name="signin",
    ),
]
