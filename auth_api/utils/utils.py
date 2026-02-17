from django.core.mail import EmailMessage
import os
# Create Your Utils : 
class util : 
    @staticmethod
    def send_email(data) : 
        email = EmailMessage(
            subject=data["subject"]  , 
            body = data["body"] ,
            from_email = os.environ.get("EMAIL_USER") ,
            to = [data["to_email"]]

        )
        email.send()

def check_roles(user_role) :
    """
    Docstring for check_roles
    
    :param user_role : get requset user role
    """

    SUPER_ADMIN_ALLOWED_LIST = ["Admin","Doctor", "Nurse",]
    ADMIN_ALLOWED_LIST = ["Doctor", "Nurse",]
    DOCTOR_ALLOWED_LIST = ["Nurse",]
    ALLOWED_LIST = []
    if "SuperAdmin" in user_role :
        ALLOWED_LIST = SUPER_ADMIN_ALLOWED_LIST
    elif "Admin" in user_role :
        ALLOWED_LIST = ADMIN_ALLOWED_LIST
    elif "Doctor" in user_role :
        ALLOWED_LIST = DOCTOR_ALLOWED_LIST
    else :
        ALLOWED_LIST = []
    return ALLOWED_LIST
    