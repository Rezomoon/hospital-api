from django.db import models
from auth_api.auth.account.models import PersonBase
from django.conf import settings
from auth_api.libs.db.models import AuditModel
# Create your models here.


class Patient(PersonBase) : 

    is_active   = models.BooleanField(default=True) # ??

    admission   = models.ManyToManyField("hospital.Hospital" , 
                                        through = "hospital.PatientAdmission",
                                        through_fields = ("patient" , "hospital")) # (source , target)
    
    # medical_record_number = models.CharField(max_length=20 , unique=True , editable=False) todo!

    
    # def get_absolute_url(self): # ToDo !?
    #     from django.urls import reverse
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta : 
        verbose_name = "Patient"
        verbose_name_plural = "Patients"


class Visit(AuditModel) : 

    doctor      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null = True)

    patient     = models.ForeignKey("Patient", on_delete=models.PROTECT, null = True)

    hospital    = models.ForeignKey("hospital.Hospital" , on_delete=models.PROTECT , null=True)

    departement = models.ForeignKey("hospital.Departement" , on_delete=models.PROTECT , null = True)

    description = models.TextField()

    # drugs       = models.ForeignKey("Drugs" , on_delete=models.PROTECT)

    visit_date    = models.DateTimeField( null = True) # Its Diffrent With created_at cause some Times should set the past date

    class Meta : 
        verbose_name = "Visit"
        verbose_name_plural = "Visits"
    
    def __str__(self):
        return f"{self.patient}"