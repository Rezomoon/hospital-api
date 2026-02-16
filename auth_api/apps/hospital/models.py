from django.db import models
from auth_api.libs.db.models import AuditModel
from django.conf import settings
# Create your models here.

class Hospital(AuditModel) : 
    name = models.CharField(max_length=150 ,)
    code = models.CharField(
        max_length=10 ,
        unique=True ,
        help_text="Short Unique Code For Hospital"
    )
    address = models.TextField(null = True, blank = True)
    phone_number = models.CharField(max_length=20 , blank=True)
    
    is_active = models.BooleanField(default=True)

    class Meta : 
        verbose_name = "Hospital"
        verbose_name_plural = "Hospitals"

    def __str__(self):
        return self.name

class Departement(AuditModel) :
    hospital = models.ForeignKey(
        Hospital , 
        on_delete=models.PROTECT , 
        related_name="departements"
    )
    name = models.CharField(max_length=150 ,)
    code = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)

    class Meta :
        unique_together = ("hospital" , "code")
        verbose_name = "Departement"
        verbose_name_plural = "Departements"

    def __str__(self):
        return f"{ self.name } az {self.hospital.name}"
    

class UserHospitalMembership(AuditModel) : 

    user        = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , null= True, related_name="userHospitals")

    hospital    = models.ForeignKey("Hospital" , on_delete=models.CASCADE , null=True)

    departement = models.ForeignKey("Departement", on_delete=models.CASCADE , null=True , blank = True ,)

    role        = models.ForeignKey("account.Role" , on_delete=models.CASCADE , null= True, related_name="roles")

    is_active   = models.BooleanField(default=True) 

    joined_at   = models.DateTimeField(auto_now_add=True , null=True)

class PatientAdmission(AuditModel) : 
    
    patient         = models.ForeignKey("Person.Patient", on_delete=models.PROTECT , null=True)

    hospital        = models.ForeignKey("Hospital" , on_delete=models.PROTECT , null=True) 

    status          = models.ForeignKey("account.Status" , on_delete=models.PROTECT , null=True)

    responsible_doctor = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.PROTECT , null= True)

    admitted_at     = models.DateTimeField(auto_now_add=True , null=True , blank= True ) # Ehtemalan beshe az field created_at ham b jaye in estefadeh kard !

    discharged_at   = models.DateTimeField(null=True, blank = True)

    # is_active = ??



