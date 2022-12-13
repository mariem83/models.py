from django.shortcuts import render
from rest_framework import generics
from product.serializer import ProductSerial
from News.serializer import NewsSerial
from standard import models
from . import Serializer
from standard import models
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class ProfilePrudect(generics.ListAPIView):
    serializer_class = ProductSerial
    def get_queryset(self):
        uid = self.kwargs['uid']
        return models.Product.objects.filter(uploaded_by=uid)
class ProfileNews(generics.ListAPIView):
    serializer_class = NewsSerial
    def get_queryset(self):
        uid = self.kwargs['uid']
        return models.News.objects.filter(uploaded_by=uid)
class VendorProfile(generics.RetrieveAPIView):
    serializer_class = Serializer.VendorSerial
    queryset = models.Vendor.objects.all()

class CustomerProfile(generics.RetrieveAPIView):
    serializer_class = Serializer.CutomerProfiel
    queryset = models.CustomerUser.objects.all()

class VendorCommentAndReplayInfo(APIView):
    def get(self, request, *args, **kwargs):
        uid = self.kwargs['uid']
        vendorCommentInfo = list(models.VendorComment.objects.filter(Commented_in_id=uid).values())
        for comment in vendorCommentInfo:
            if models.VendorReply.objects.filter(comment_id_id=comment.get('id')).exists():
                comment['replies'] = list(models.VendorReply.objects.filter(comment_id_id=comment.get('id')).values())

        return Response(vendorCommentInfo)




class CreateComment(generics.CreateAPIView):
    serializer_class = Serializer.VendorCommentSer
    queryset = models.VendorComment.objects.all()


class CreateReaplay(generics.CreateAPIView):
    serializer_class = Serializer.VendorReplay
    queryset = models.VendorReply.objects.all()





class CreateVendorComment(APIView):
    def post(self, request, *args, **kwargs):
        serializer = Serializer.VendorCommentSer(data=request.data)
        if serializer.is_valid():
            comment = serializer.validated_data
            if comment.get("User_id") != comment.get("Commented_in"):
                serializer.save()
                return Response('{"message":"created"}', status=201)
            else:
                return Response('{"message":"Commenting user can not be the vendor himself"}', status=400)
        else:
            return Response('{"message":"not valid comment data"}', status=400)