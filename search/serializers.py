from rest_framework import serializers
from standard import models


class VendorSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'shop_title', 'shop_desc', 'shop_img_url']


class VendorSerialPlus(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['shop_title']


class SearchSerial(serializers.ModelSerializer):

    shop_title = VendorSerialPlus(source='Vendor', read_only=True)

    class Meta:
        model = models.Product
        fields = ['prod_name', 'shop_title', 'in_category', 'price', 'price_type', 'uploaded_by', 'prod_img_url']



