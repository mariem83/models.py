from rest_framework import generics
from . import serializer
from standard import models


class CreateProduct(generics.CreateAPIView):
    serializer_class = serializer.ProductSerial


class GetProductDetail(generics.RetrieveAPIView):
    serializer_class = serializer.ProductSerial
    queryset = models.Product.objects.all()


class GetProductList(generics.ListAPIView):
    serializer_class = serializer.ProductSerial
    queryset = models.Product.objects.all()


class GetCategoryList(generics.ListAPIView):
    serializer_class = serializer.CategorySerial
    queryset = models.Category.objects.all()
