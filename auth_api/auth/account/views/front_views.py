from rest_framework.response import Response
from rest_framework.views import APIView 
from auth_api.auth.account.serializers.user_serializers import (ProfileSerializers , UpdatePassworddSerializer, AdminRegistrationSerializer, UpdateUserSerializer)
from rest_framework import status
# Create Your Views : 


class UserProfile(APIView) :

    def get(self , request) : 
        user        = request.user
        serializer  = ProfileSerializers(user)
        return Response({
            "data" : serializer.data
        } , status=status.HTTP_200_OK)
    
    def put(self , request) : 
        user        =  request.user   
        data        = request.data
        if data.get("password") :
            serializer  = UpdatePassworddSerializer(user , data, partial = True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        serializer  = UpdateUserSerializer(user , data ,partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()   
        serializer = ProfileSerializers(user)
        return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
