from rest_framework import generics
from . import serializers
from standard import models


class CreateNotification(generics.CreateAPIView):
    serializer_class = serializers.NotificationSerial


class ListNotification(generics.ListAPIView):
    serializer_class = serializers.NotificationSerial
    queryset = models.Notification.objects.all()

    def get_queryset(self):
        user_id = self.kwargs['pk']
        result = models.Notification.objects.filter(User_id=user_id)
        return result


class RetrieveNotification(generics.RetrieveAPIView):
    serializer_class = serializers.NotificationDetailSerial
    queryset = models.Notification.objects.all()