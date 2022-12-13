from django.shortcuts import render
from rest_framework import generics
from . import serializer
from standard import models
class GetNews(generics.ListAPIView):
    serializer_class = serializer.NewsSerial
    queryset = models.News.objects.all()
class CreateNews(generics.CreateAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializer.NewsSerial



