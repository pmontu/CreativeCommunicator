"""api"""
# from django.shortcuts import render
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(ModelViewSet):
    """messages api"""
    serializer_class = MessageSerializer
    model = Message
    filterset_fields = ['sender__email', 'recipients__email']

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(
            Q(sender=user) | Q(recipients=user)
        )

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
