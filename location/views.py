from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from . import serializer
from standard import models
from django.contrib.auth import get_user_model



class CreateLocation(generics.CreateAPIView):
    serializer_class = serializer.LocationSerial


class GetLocation(generics.RetrieveAPIView):
    serializer_class = serializer.LocationSerial
    queryset = models.Location.objects.all()


class UpdateLocation(APIView):
    def put(self, request, format=None, **kwargs):
        MakeNormalLocation=models.Location.objects.all().update(
        main_location=0,
   )
        MakePrimarylocation = models.Location.objects.filter(
            pk=kwargs['pk']
        ).update(
            main_location=1,
        )
        if(MakePrimarylocation==1):
            return Response({"message": "Update"})
        else:
            return Response({"message": "InValid Try Again"})


class GetLocationList(generics.ListAPIView):
    serializer_class = serializer.LocationSerial
    queryset = models.Location.objects.all().order_by('-main_location')


class DelLocation(generics.DestroyAPIView):
    serializer_class = serializer.LocationSerial
    queryset = models.Location.objects.all()




class GetPrimaryLocation1(APIView):
    serializer_class = serializer.LocationSerial

    def get (self, request, format=None, **kwargs):
     Id = self.kwargs['UserId']
     owner = get_user_model().objects.get(id=Id)
     query=models.Location.objects.filter(owner=owner,main_location=1)

     serializerclass = serializer.LocationSerial(query, many=True)
     return Response(serializerclass.data)