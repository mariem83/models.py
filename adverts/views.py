from rest_framework import generics
from standard import models
from . import serializers


class UploadAds(generics.CreateAPIView):
    serializer_class = serializers.AdsSerial
    queryset = models.AdvertsPro.objects.all()


class RetrieveAds(generics.RetrieveAPIView):
    serializer_class = serializers.AdsSerial
    queryset = models.AdvertsPro.objects.all()
