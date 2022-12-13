from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework import generics
from tornado.platform.twisted import _

from . import Serializers
from standard import models
from django.contrib.auth import get_user_model


class CreateCart(generics.CreateAPIView):
    queryset = models.Cart.objects.all()
    serializer_class = Serializers.CartSerializer

    def create(self, request, *args, **kwargs):
        if models.Cart.objects.filter(owner=self.request.data.get("owner"), product=request.data.get("product")).exists():
            return Response({"id": "Token Not Valid"})
        else:
            return super().create(request, *args, **kwargs)


class GetCart(generics.ListAPIView):
    serializer_class = Serializers.CartSerializer
    #queryset = models.Cart.objects.filter(owner=owner)

    def get_queryset(self):
        Id = self.kwargs['UserId']
       # Id =self.request.data.get("UserId")
        owner = get_user_model().objects.get(id=Id)
        return models.Cart.objects.filter(owner=owner)


class DeleteCart(generics.DestroyAPIView):
    serializer_class = Serializers.CartSerializer
    queryset = models.Cart.objects.all()
