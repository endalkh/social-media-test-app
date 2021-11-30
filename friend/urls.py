from django.urls import path
from friend import views

app_name = "friend"
urlpatterns = [
    path("friends", views.Friend_LA.as_view()),
    path("friends/<str:id>", views.Friend_RUD.as_view()),
]
