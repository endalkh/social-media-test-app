from django.contrib import admin
from authentication import models as authentication

auth_model = [
    authentication.User,
]

admin.site.register(auth_model)
