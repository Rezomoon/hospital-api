from django.db import models
from django.conf import settings

# # Create Your Abstract Model : 


class AuditModel(models.Model) : 

    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null = True , related_name= "+" , editable=False) 
    created_at  = models.DateTimeField(auto_now_add=True ,null=True , editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL , null = True ,  related_name= "+" , editable=False)  # Va Chon 2ta field dar b 1 model fk mikhore hatman bayad az related_name estefadeh shavad
    updated_at = models.DateTimeField(auto_now=True , editable=False , null=True ,)
    class Meta : 
        abstract = True
