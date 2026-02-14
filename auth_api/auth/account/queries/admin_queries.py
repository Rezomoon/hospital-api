from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
# Create Your Queries : 

def get_user(id) : 
    try :
        user = get_user_model().objects.get(id = id)
        print(type(user))
        return user
    except get_user_model().DoesNotExist :
        return Response({"errors" : "USER DOESE NOT EXIST!"} , status=status.HTTP_404_NOT_FOUND)