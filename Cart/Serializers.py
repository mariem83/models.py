from rest_framework import serializers


from standard import models
from product.serializer import ProductSerial
class CartSerializer(serializers.ModelSerializer):
    productinfo=ProductSerial(source='product',read_only=True)
    class Meta:
        model= models.Cart
        fields = ['owner','product','id','productinfo']