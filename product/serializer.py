from rest_framework import serializers
from standard import models
#from Auth.Serializers import UserSerializer

class ProductSerial(serializers.ModelSerializer):
    #UserInfo=UserSerializer(source='uploaded_by',read_only=True)
    class Meta:
        model = models.Product
        fields = '__all__'

class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'