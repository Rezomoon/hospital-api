from rest_framework.response import Response 
from rest_framework import status
from rest_framework.views import APIView
from auth_api.auth.account.serializers.back_serializers import AdminRegistrationSerializer , LoginSerailizer , BasicUserSerailizer
from django.contrib.auth import authenticate
from auth_api.auth.account.renderers import CustomRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated , AllowAny

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
    def post(sefl , request) : 
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

def get_tokens_for_user(user) : 
    refresh = RefreshToken.for_user(user)
    return {
        'refresh'   : str(refresh) , 
        'access'    : str(refresh.access_token) ,
    }