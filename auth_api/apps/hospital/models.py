from django.db import models

# Create your models here.

class Hospital(models.Model) : 
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

class Departement(models.Model) :
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
