from rest_framework import serializers
from standard import models


class OrderSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'