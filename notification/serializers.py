from rest_framework import serializers
from standard import models


class NotificationSerial(serializers.ModelSerializer):

    class Meta:
        model = models.Notification
        fields = ['User_id', 'title', 'reached_in']


class NotificationDetailSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
