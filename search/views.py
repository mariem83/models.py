from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Q
from . import serializers
from standard import models


class SearchProductName(generics.ListAPIView):
    serializer_class = serializers.SearchSerial
    queryset = models.Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        lookup = Q(prod_name__icontains=q)
        results = models.Product.objects.none()
        if q is not None:
            results = qs.filter(lookup)
        return results


class SearchProductCategory(generics.ListAPIView):
    serializer_class = serializers.SearchSerial
    queryset = models.Product.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        lookup = Q(in_category__category_name__icontains=q)
        results = models.Product.objects.none()
        if q is not None:
            results = qs.filter(lookup)
        return results


# will search for Shop_Title and userID not the product

class SearchProductShopName(generics.ListAPIView):
    serializer_class = serializers.VendorSerial
    queryset = models.Vendor.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        lookup = Q(shop_title__icontains=q)
        results = models.Vendor.objects.none()
        if q is not None:
            results = qs.filter(lookup)
        return results



