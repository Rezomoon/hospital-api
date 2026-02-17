from rest_framework import serializers
from auth_api.apps.hospital.models import (UserHospitalMembership ,
                                           Departement,
                                           Hospital
                                           )
from .base_serializers import DepartementSerializers
# from auth_api.auth.account.serializers.user_serializers import BasicUserDataSerializers

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
class HospitalMemberShipsCustomSerializer(serializers.ModelSerializer) : 
    # ! Should Check With Ai Cause When I want to import :
    # from auth_api.auth.account.serializers.user_serializers import BasicUserDataSerializers
    # ! it has Error So I Do It Like This :

    user_id     = serializers.IntegerField(source = "user.id" , read_only = True)
    status      = serializers.CharField(source = "user.status" , read_only = True)
    email       = serializers.EmailField(source = "user.email" , read_only = True)
    person_code = serializers.CharField(source = "user.person_code" , read_only = True)
    full_name   = serializers.CharField(source = "user.full_name" , read_only = True)
    role        = serializers.CharField(source = "role.name" , read_only = True)
    class Meta : 
        model = UserHospitalMembership 
        fields = [
            "id", 
            "user_id" ,
            "status" ,
            "email" ,
            "person_code" ,
            "full_name" ,
            "role" ,
            "is_active" ,
        ]
class UserHospitalDetailsSerializer(serializers.ModelSerializer) :
    departements = DepartementSerializers(read_only = True , many = True)
    class Meta : 
        model = Hospital
        fields = "__all__"