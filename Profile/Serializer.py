from rest_framework import serializers

from standard import models

from location.serializer import ShoplocationSerial


class VendorSerial(serializers.ModelSerializer):
    ShopLocation = ShoplocationSerial(source='shoplocation', read_only=True)

    class Meta:
        model = models.Vendor
        fields = '__all__'
class CutomerProfiel(serializers.ModelSerializer):
    UserInfo = ShoplocationSerial(source='Userid', read_only=True)
    class Meta:
        model = models.CustomerUser
        fields = '__all__'
class VendorCommentSer(serializers.ModelSerializer):
    class Meta:
        model = models.VendorComment
        fields = '__all__'


class VendorReplay(serializers.ModelSerializer):
    class Meta:
        model = models.VendorReply
        fields = '__all__'
