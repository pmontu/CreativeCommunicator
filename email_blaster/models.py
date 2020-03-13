from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    subject = models.TextField()
    text = models.TextField()
    recipients = models.ManyToManyField(User, related_name="messages")
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    sent_on = models.DateTimeField(auto_now_add=True)
