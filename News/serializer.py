from rest_framework import serializers
from standard import models


class NewsSerial(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'