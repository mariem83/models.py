from rest_framework import serializers
from standard import models


class LocationSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'
class ShoplocationSerial(serializers.ModelSerializer):
    class Meta:
        model = models.ShopLocation
        fields = '__all__'