from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView

from auth_api.auth.account.serializers.user_serializers import (AdminRegistrationSerializer , LoginSerailizer ,
                                                                BasicUserSerailizer, SentResetPasswordEmailSerializer,
                                                                UserPasswordResetSerializer, )

from django.contrib.auth import authenticate
from auth_api.auth.account.renderers import CustomRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken

# Create Your View APIs : 

class UserRegistration(APIView) :
    # renderer_classes = [CustomRenderer]
    def post(self , request, format = None) :
        data        = request.data
        serializer  = AdminRegistrationSerializer(data = data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user=user   )
        return Response({
            "token" : token ,
            "user"  : serializer.data} ,
            status = status.HTTP_201_CREATED)

class LoginAPI(APIView) : 
    # renderer_classes = [CustomRenderer]
    permission_classes = [AllowAny , ]
    def post(self , request) : 
        data = request.data
        serializer = LoginSerailizer(data = data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email = email , password = password)
        if user :
            user_serializer = BasicUserSerailizer(user) 
            token = get_tokens_for_user(user)
            return Response(
                {
                "token"     : token , 
                "user"      : user_serializer.data ,
                } ,
                status= status.HTTP_202_ACCEPTED)
        elif user is None :
            
            return Response({
                "msg"   : "EMAIL OR PASSWORD IS INCORRECT !"
            } ,status=status.HTTP_404_NOT_FOUND)

class LogoutUser(APIView) : 
    def post(self , request, format = None) : 
        try : 
            refresh_token   = request.data.get("refresh_token")
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response({"msg" : "LOGOUT SECCESSFULLY "} , status=status.HTTP_205_RESET_CONTENT)
        except Exception as e : 
            return Response(e,status=status.HTTP_404_NOT_FOUND)
class SentResetPasswordEmail(APIView) :
    permission_classes = [AllowAny] 
    def put(self, request) :
        data = request.data
        serializer = SentResetPasswordEmailSerializer(data = data)
        serializer.is_valid(raise_exception=True )
        return Response({
            "msg" : "Email Sent !"
        } , status=status.HTTP_200_OK)

class UserPasswordReset(APIView) : 
    permission_classes = [AllowAny] 
    def put(self, request, uid, token) :
        data    = request.data
        # user      = check_uid_reset_password(uid=uid , token=token)   
        serializer = UserPasswordResetSerializer( data = data, context = {"uid" : uid , "token" : token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg" : serializer.data} , status=status.HTTP_202_ACCEPTED)


def get_tokens_for_user(user) : 
    refresh = RefreshToken.for_user(user)
    return {
        'refresh'   : str(refresh) , 
        'access'    : str(refresh.access_token) ,
    }

