from django.db import models
from authentication import models as authentication
import uuid


class Friendship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    _from = models.ForeignKey(
        authentication.User, related_name="_from", on_delete=models.CASCADE
    )
    _to = models.ForeignKey(
        authentication.User, related_name="_to", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
