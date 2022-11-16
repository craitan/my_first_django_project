from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

UserModel = get_user_model()


class Room(models.Model):
    MAX_LEN_CHAT_NAME = 200
    name = models.CharField(
        max_length=MAX_LEN_CHAT_NAME,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class Message(models.Model):
    value = models.CharField(
        max_length=300,
    )
    date = models.DateTimeField(
        default=datetime.now,
        blank=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.RESTRICT,
    )
