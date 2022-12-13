from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from rest_framework import generics
from django.contrib.auth import get_user_model

from standard import models
from django.db import transaction
# Create your views here.



class CraeteOrder(generics.CreateAPIView):

    serializer_class = serializers.OrderSerial



class CraeteOrder2(APIView):

    def post(self, request):
        token = request.data.get("OrderItemid")['prod_name']
        print(token)
        with transaction.atomic():
         Customer = get_user_model().objects.get(id=request.data.get("customer_id"))
         order1= models.Order.objects.create(customer_id=Customer,order_state=request.data.get("order_state"),Total_price=request.data.get("Total_price"),order_quantity=request.data.get("order_quantity"))
         item=models.OrderItem.objects.create(prod_name=request.data.get("OrderItemid")['prod_name'],price=request.data.get("OrderItemid")['price'],prod_img_url=request.data.get("OrderItemid")['prod_img_url'],product_quantity=request.data.get("OrderItemid")['product_quantity'],order_id=order1)

        return Response({"message": "Token Not Valid"})

        # with transaction.atomic():


            #models.Order.objects.create()



class OrderInfo(APIView):
    def get(self, request, *args, **kwargs):
        uid = self.kwargs['uid']
        ordersInfo = list(models.Order.objects.filter(customer_id__id=uid).values())
        for order in ordersInfo:
            if models.OrderItem.objects.filter(order_id__id=order.get('id')).exists():
                order['order_items'] = list(models.OrderItem.objects.filter(order_id__id=order.get('id')).values())
        return Response(ordersInfo)