from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from auth_api.apps.hospital.queries.departement_queries import (
                                                                get_user_departement,
                                                                
                                                                )
from auth_api.apps.hospital.serializer.base_serializers import (
                                                                DepartementSerializers
                                                                )
# Create Your APIs Here : 
class UserDeopartements(APIView) : 

    def get(self, requst) : 
        user = requst.user
        query = get_user_departement(user)
        serializer = DepartementSerializers(query , many = True)
        data = {
            "data" :serializer.data
        }
        return Response(data ,status=status.HTTP_200_OK)
    