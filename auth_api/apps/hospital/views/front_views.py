from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth_api.apps.hospital.queries.hospital_queries import (get_hospital_by_id , 
                                                            get_UserHospitalMembership_by_hospital_id,
                                                            user_hospitals ,)
from auth_api.apps.hospital.serializer.base_serializers import (UserHospitalMembershipSerializers ,
                                                                HospitalSerializers
                                                                )
from auth_api.apps.hospital.serializer.custom_serializer import (
                                                                UserHospitalMemberShipCustomSerializer ,
                                                                HospitalMemberShipsCustomSerializer,
                                                                UserHospitalDetailsSerializer ,
                                                                )
from auth_api.auth.account.permissions.basic_permissions import (
                                                                # IsAdminOrSuperUser , 
                                                                NotNurse ,
                                                                HasThisHospital)
# Create your views here.
class HospitalMemberShipsAPIView(APIView) :

    permission_classes = [NotNurse]

    def get(self , request , hospital_id) :
        user = request.user
        query = get_UserHospitalMembership_by_hospital_id(user , hospital_id=hospital_id)
        serializer = HospitalMemberShipsCustomSerializer(query , many = True)
        data = {
            "data" : serializer.data
        }
        return Response(data , status  = status.HTTP_200_OK)
    
class UserHospitals(APIView) : 
    def get(self , request) : 
        user = request.user
        query = user_hospitals(user)
        serializer = HospitalSerializers(query , many = True)
        data = {
            "data" : serializer.data
        }
        return Response(data , status = status.HTTP_200_OK)
    
class UserHospitalDetails(APIView) :
    permission_classes = [HasThisHospital]
    def get(self,request, hospital_id) :
        query   = get_hospital_by_id(hospital_id)

        self.check_object_permissions(request , query )

        serializer = UserHospitalDetailsSerializer(query )

        data = {
            "data" : serializer.data
        }

        return Response(data ,status=status.HTTP_200_OK)