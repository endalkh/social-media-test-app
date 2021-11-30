from django.contrib import admin
from friend import models as friend

friend_model = [
    friend.Friendship,
]

admin.site.register(friend_model)
