from rest_framework.response import Response
from rest_framework.views import APIView 
from auth_api.auth.account.serializers.user_serializers import (ProfileSerializers , UpdatePassworddSerializer, UpdateUserSerializer ,BasicUserSerailizer)
from rest_framework import status
from auth_api.auth.account.queries.admin_queries import (get_user_hospitals_id ,get_user_list_by_hospital_id,
                                                         get_user , get_role_hospitals_id)
from auth_api.auth.account.permissions.basic_permissions import NotNurse , SameHospital
from django.shortcuts import get_object_or_404
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
    permission_classes = [NotNurse , ]
    def get(self ,request, hospital_id) :

        """

        Get Users List  of The Specified Hospital

        """

        user= request.user
        query = get_user_list_by_hospital_id(user , hospital_id)
        serializer = BasicUserSerailizer(query ,many = True)
        data = {
            "data" : serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

class UserDetailsByIdAPIView(APIView) :
    permission_classes = [SameHospital]
    def get(self ,request , user_id) :
        users_query = get_user(user_id)
        self.check_object_permissions(request , users_query)
        serializer = BasicUserSerailizer(users_query )
        return Response(serializer.data)
    
    def put(self , request , user_id) : 
        user = get_user(user_id)
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


