from rest_framework import serializers
from auth_api.apps.hospital.models import (UserHospitalMembership ,Departement)
from .base_serializers import DepartementSerializers

# Create Your Custom Serializer : 

class DepartementCustomSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Departement
        fields = ("id",
                  "name",
                  "code",)
class UserHospitalMemberShipCustomSerializer(serializers.ModelSerializer) :
    hospital_name       = serializers.CharField(source      = "hospital.name", read_only = True)
    hospital_id         = serializers.IntegerField(source   = "hospital.id" , read_only = True)
    hospital_code       = serializers.CharField(source = "hospital.code" , read_only = True)                                                   

    departement_id      = serializers.IntegerField(source   = "departement.id" , read_only = True)
    departement_name    = serializers.CharField(source =  "departement.name", read_only = True)

    role_id             = serializers.IntegerField(source   = "role.id" , read_only = True)
    role_name           = serializers.CharField(source   = "role.name" , read_only = True)
    
    class Meta : 

        model   = UserHospitalMembership

        fields  = ( "hospital_id",
                    "hospital_name",
                    "hospital_code" ,
                    "departement_id" ,
                    "departement_name",
                    "is_active" ,
                    "role_id" ,
                    "role_name" ,
                    
                    )
