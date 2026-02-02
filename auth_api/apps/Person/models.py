from django.db import models
# from auth_api.libs.db.models import PersonBase
from auth_api.auth.account.models import PersonBase
# Create your models here.


class Patient(PersonBase) : 

    is_active = models.BooleanField(default=True)
    # medical_record_number = models.CharField(max_length=20 , unique=True , editable=False)
    # departemant
    def __str__(self):
        return self.first_name + " " + self.last_name
    class Meta : 
        verbose_name = "Patient"
        verbose_name_plural = "Patients"