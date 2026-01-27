from django.db import models
from django.conf import settings

# Create Your Abstract Model : 


class BasicUserModel(models.Model) :

    
    first_name  = models.CharField(max_length=150 , blank=True  )
    last_name   = models.CharField(max_length=150 , blank=True  )
    
    date_of_birth   = models.DateField(null=True , blank= True)
    weight          = models.PositiveIntegerField(null= True , blank= True)
    height          = models.PositiveIntegerField(null= True , blank= True)
    

    person_code     = models.CharField(max_length=6) # todo?
    # in yek code hastesh baraye ham mariz va ham users(code mariz) va code personeli

    # ImageField =

    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.SET_NULL , null = True , related_name= "created" , editable=False) 
    created_at  = models.DateTimeField(auto_now_add=True , editable=False)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL , null = True ,  related_name= "modified" , editable=False)  # Va Chon 2ta field dar b 1 model fk mikhore hatman bayad az related_name estefadeh shavad
    updated_at = models.DateTimeField(auto_now=True , editable=False)

    class Meta : 
        abstract = True