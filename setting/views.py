from rest_framework import generics
from . import serializer
from standard import models
from django.contrib.auth.models import User


class VendorUpdate(generics.UpdateAPIView):
    serializer_class = serializer.VendorSerial
    queryset = models.Vendor.objects.all()


class shop_location_Update(generics.UpdateAPIView):
    serializer_class = serializer.shop_locSerial
    queryset = models.ShopLocation.objects.all()




class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = serializer.ChangePasswordSerializer
