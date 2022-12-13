from rest_framework import serializers
from standard import models


class AdsSerial(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertsPro
        fields = '__all__'
