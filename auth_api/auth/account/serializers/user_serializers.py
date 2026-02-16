from rest_framework import serializers 
from django.contrib.auth import get_user_model # Its For Import User

# These Are For Send ResetPassword Links
from xml.dom import ValidationErr
from django.utils.encoding import smart_str , force_bytes , DjangoUnicodeDecodeError 
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from auth_api.auth.account.queries.admin_queries import get_user
from auth_api.auth.account.models import BaseCustomUser
from auth_api.utils.utils import util
from auth_api.apps.hospital.serializer.base_serializers import HospitalSerializers
from auth_api.apps.hospital.serializer.custom_serializer import UserHospitalMemberShipCustomSerializer
# Create Your Serailizers : 

class ProfileSerializers(serializers.ModelSerializer) : 
    class Meta : 
        model  = get_user_model()
        fields = "__all__"

class BasicUserSerailizer(serializers.ModelSerializer) : 
    hospital = UserHospitalMemberShipCustomSerializer(
        many = True ,
        source = "userHospitals" ,
        read_only = True,
        )

    status      = serializers.CharField(source = 'status.name' , read_only = True)
    # hospital    = HospitalSerializers(many = True, read_only = True)
    class Meta : 
        model = get_user_model()
        fields = ["id" ,
                  "first_name" ,
                  "last_name",
                  "is_admin",
                  "is_staff",
                  "is_superuser",
                  "person_code",
                  "last_login",
                  "status" ,
                  "hospital",
                  ]

class AdminRegistrationSerializer(serializers.ModelSerializer) : 
    password2 = serializers.CharField(style = {"input_type" : "password"} , write_only = True)
    class Meta : 
        model   = get_user_model()
        fields  = ["email", "username","password","password2"] 
        extra_kwargs = {
            "username"      : {"required" : True} ,
            "email"         : {"required" : True} ,
            "password"      : {"write_only" : True} ,
        }
    def validate(self, attrs) : 
        password    = attrs.get("password") 
        password2   = attrs.get("password2")
        if password != password2 : 
            raise serializers.ValidationError("PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH !")
        return attrs
    def create(self, validated_data) :
        return get_user_model().objects.create_admin(**validated_data)
    

class UpdatePassworddSerializer(serializers.ModelSerializer) :
    password2 = serializers.CharField(style = {"input_type" : "password"} , write_only = True)
    class Meta : 
        model   = get_user_model()
        fields  = ["password" , "password2"]
        extra_kwargs = {
            "password"      : {"write_only" : True} ,
        }
    def validate(self, attrs) : 
        password    = attrs.get("password") 
        password2   = attrs.get("password2")
        if password != password2 : 
            raise serializers.ValidationError("PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH !")
        return attrs
    def update(self, instance, validated_data):
        instance.set_password = validated_data["password"]
        instance.save()
        return instance
class UpdateUserSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model   = get_user_model()
        fields  = ["email", "username", "first_name", "last_name",]
    
class LoginSerailizer(serializers.ModelSerializer) :
    email       = serializers.EmailField(max_length = 150 ,)
    class Meta : 
        model   = get_user_model()
        fields  = ["email" , "password"]

class SentResetPasswordEmailSerializer(serializers.Serializer) : 
    email = serializers.EmailField(max_length = 255 , )
    class Meta : 
        model   = get_user_model()
        fields  = ["email" ,]
    def validate(self, attrs):
        email = attrs.get("email")
        if get_user_model().objects.filter(email = email).exists() : 
            user = get_user_model().objects.get(email = email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("FORCE_BYTES : " , force_bytes(user.id))
            print("ENCODED UID : " , uid)
            token = PasswordResetTokenGenerator().make_token(user=user)
            print("TOKEN IS : " , token)
            link = "http://localhost:3000/api/reset/" + uid + "/" +token
            print("LINK IS : " , link)
            body = "Click Following Link to Reset Password"
            data = {
                "subject" : "Reset Your Passowrd", 
                "body" : body , 
                "to_email" : user.email
            }
            # util.send_email(data)
            return attrs
        else : 
            raise ValueError("CANT FIND THE EMAIL !")
        


class UserPasswordResetSerializer(serializers.Serializer) :
    """
    Docstring for UserPasswordResetSerializer: 
    Its Like UpdatePassworddSerializer But Just For The Futre Develope => Crate new serializer 

    """
    password = serializers.CharField(style = {"input_type" : "password"} , write_only = True)
    password2 = serializers.CharField(style = {"input_type" : "password"} , write_only = True)
    class Meta : 
        model   = get_user_model()
        fields  = ["password" , "password2"]
        extra_kwargs = {
            "password"      : {"write_only" : True} ,
        }
    def validate(self, attrs) : 
        password    = attrs.get("password") 
        password2   = attrs.get("password2")
        uid     = self.context.get("uid")
        token   = self.context.get("token")

        if password != password2 :
            raise serializers.ValidationError("PASSWORD AND CONFIRM PASSWORD DOES NOT MATCH !")
        id  = smart_str(urlsafe_base64_decode(uid))
        user = get_user(id=id)
        print("user : " , user)
        if not PasswordResetTokenGenerator().check_token(user , token) : 
            raise ValueError("TOKEN IS NOT VALID !")
        user.set_password(password)
        user.save()
        return attrs