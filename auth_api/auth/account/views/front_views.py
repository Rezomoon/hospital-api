from rest_framework.response import Response
from rest_framework.views import APIView 
from auth_api.auth.account.serializers.user_serializers import (ProfileSerializers , UpdatePassworddSerializer, UpdateUserSerializer ,BasicUserSerailizer)
from rest_framework import status
from auth_api.auth.account.queries.admin_queries import (get_user_hospitals_id ,get_user_list)
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


class UserListAPIView(APIView) : 
    def get(self ,request) : 
        user= request.user
        query = get_user_hospitals_id(user)
        query2 = get_user_list(user , )
        serializer = BasicUserSerailizer(query2 ,many = True)
        data = {
            "data"  : str(query) ,
            "data2" : str(query2) ,
            "ser_data" : serializer.data
        }
        return Response(data=data)