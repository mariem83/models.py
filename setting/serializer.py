from rest_framework import serializers
from standard import models
from django.contrib.auth.models import User


class VendorSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ('identification_img_url','commercial_registration','mobile_num','shop_title','shop_img_url','shop_desc')


class shop_locSerial(serializers.ModelSerializer):
    class Meta:
        model = models.ShopLocation
        fields = ('shop_email','country','city','street_floor_apartment','postal_code')


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password_confirm')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
