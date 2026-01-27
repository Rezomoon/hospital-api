from rest_framework import serializers 
from django.contrib.auth import get_user_model # Its For Import User
# Create Your Serailizers : 

class BasicUserSerailizer(serializers.ModelSerializer) : 
    class Meta : 
        model = get_user_model()
        fields = ["first_name" , "last_name", "is_admin", "is_staff", "is_superuser", "person_code", "last_login"]
class AdminRegistrationSerializer(serializers.ModelSerializer) : 
    password2 = serializers.CharField(style = {"input_type" : "password"} , write_only = True)
    class Meta : 
        model   = get_user_model()
        fields  = ["email", "username", "password","password2"] 
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
        print(validated_data)
        return get_user_model().objects.create_admin(**validated_data)
    
class LoginSerailizer(serializers.ModelSerializer) :
    email       = serializers.EmailField(max_length = 150 ,)
    class Meta : 
        model   = get_user_model()
        fields  = ["email" , "password"]