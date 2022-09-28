from django.shortcuts import render
from django.http import HttpResponse
from home_page.models import Category,Banner
from rest_framework.response import Response
from rest_framework.views import APIView
from home_page.serializer import CategorySerializer,BannerSerializer
from rest_framework import status
from django.db.models import Q


# Create your views here.

class ProductCategory(APIView):
    
    def get(self,request,*args, **kwargs):
        get_all = Category.objects.all()
        serialize = CategorySerializer(get_all,many=True)
          
        product_price = Category.objects.all('price').order_by 
        print(product_price)

      
        content = {
            "status":status.HTTP_200_OK,
            "success":True,
            "response":serialize.data,
         
        }

        return Response(content,status=status.HTTP_200_OK)

class HomeBanner(APIView):

    def get(self,request,*args, **kwargs):
        get_all = Banner.objects.all()
        serialize = BannerSerializer(get_all,many=True)
        content = {
            "status":status.HTTP_200_OK,
            "success":True,
            "response":serialize.data
        }
        
        return Response(content,status=status.HTTP_200_OK)
