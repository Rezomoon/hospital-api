from django.utils.encoding import smart_str  
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from auth_api.auth.account.queries.admin_queries import get_user

# Create Your Utils : 

def check_uid_reset_password (uid , token) : 
    try : 
        id  = smart_str(urlsafe_base64_decode(uid))
        user = get_user(id = int(id))
        if not PasswordResetTokenGenerator().check_token(user , token) : 
            raise ValueError("TOKEN IS NOT VALID !")
        print("retrun1")
        return user
    except ValueError :
        raise ValueError("UID ERROR")