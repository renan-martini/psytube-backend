from django.db import models
import uuid


class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=128)
    thumbnail = models.CharField(max_length=128)
    link = models.CharField(max_length=128)
    downloads = models.PositiveIntegerField(default=0)
    users = models.ManyToManyField(
        "users.User", on_delete=models.CASCADE, related_name="videos"
    )
    ...
