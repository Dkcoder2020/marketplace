from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import status
from django.http import HttpResponse
from user_application.serializer import CustomUserSerializer
# Create your views here.

class UserRegister(APIView):
    # def get(self , request, *args, **kwargs):
    #     pass


    def post(self , request , *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            context ={
                "status": status.HTTP_200_OK,
                "success":True
            }

            return Response(context,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST,)
        