from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager 
from django.utils.translation import gettext_lazy as _
import string
import random
from django.db import IntegrityError
from django.conf import settings
from auth_api.libs.constants.genders import GenderChoices
from auth_api.libs.db.models import AuditModel

# Create your models here.


class Role(models.Model) : 
    name        = models.CharField(max_length=150 , unique=True)
    description = models.TextField( blank=True)
    def __str__(self):
        return self.name
    
class Status(models.Model) :
    name        = models.CharField(max_length=150 , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    def __str__(self):
        return self.name
    
class PersonBase(AuditModel) :

    first_name  = models.CharField(max_length=150 , blank=True  )
    last_name   = models.CharField(max_length=150 , blank=True  )  
    gender      = models.CharField(max_length=8 ,choices=GenderChoices.choices, default=GenderChoices.Male, )
    date_of_birth   = models.DateField(null=True , blank= True)
    weight          = models.PositiveIntegerField(null= True , blank= True)
    height          = models.PositiveIntegerField(null= True , blank= True)
    
    
    person_code     = models.CharField(max_length=6 , unique=True ,null= True ,  editable=False )
    # in yek code hastesh baraye ham mariz va ham users(code mariz) va code personeli

    # ImageField =
    # national_id

    status  = models.ForeignKey(Status ,  on_delete=models.PROTECT,null=True,blank=True,related_name="+" )
    
    @property
    def full_name(self) : 
        return self.first_name + " " +self.last_name
    
    class Meta : 
        abstract = True


class CustomeUserManager(BaseUserManager) : 
    def _create_user(self ,username , email , password = None  , **extra_fields) :
        
        if not email :
            raise ValueError("EMAIL NOT FOUND !")
        if not username  :
            raise ValueError("USERNAME NOT FOUND !")
        if not extra_fields.get("person_code") : 
            extra_fields["person_code"]  = self._generate_unique_person_code()

        
        email = self.normalize_email(email=email)
        username = self.model.normalize_username(username=username)
        user = self.model( email = email , username = username,**extra_fields)
        user.set_password(password)
        try : 
            user.save(using=self._db)
        except IntegrityError : 
            extra_fields["person_code"] = self._generate_unique_person_code()
            user.person_code = extra_fields["person_code"]
            user.save(using=self._db)
        return user

    def create_superuser(self , email  , username  , password = None  , **extra_fields) : 
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_superuser" , True)
        return self._create_user(username = username , email=email , password=password , **extra_fields)
    
    def create_admin(self, email, username, password = None, password2 = None,**extra_fields) :
        extra_fields.setdefault("is_admin" , True)
        return self._create_user(username=username , email=email, password=password, **extra_fields)
    

    def create_user(self,email,username,password = None , password2 = None, **extera_fields) :
        """
        Docstring for create_user
        
        :param email: Get Email Address
        :param username: Get UserName
        :param password: Get Password
        :param password2: Get password2 For Checking the passwords
        :param extera_fields: Description
        """
        return self._create_user(username=username, email=email, password=password , )    
    
    def _generate_unique_person_code (self,) : 
        while True : 
            code = "".join(random.choices(string.digits, k =6)) 
            if not self.model.objects.filter(person_code = code).exists() : 
                return code


class BaseCustomUser(AbstractBaseUser , PersonBase ) : 
   
    email       = models.EmailField( blank=True  ,  unique=True , null= False )
    username    = models.CharField(max_length=100 , blank= True , null= True , unique= True)

    # fk default_snf or default hospitals
    

    is_admin        = models.BooleanField(default=False) 
    is_staff        = models.BooleanField(default=False) # It Allows To Login To Django Admin(Even Can Login But is_superuser== False)=>Cant Do anything
    is_superuser    = models.BooleanField(default=False) # It Allow To Has permission(Cant log in to django admin if is_staff== False)
    is_active       = models.BooleanField(default=True)

    
    hospital        = models.ManyToManyField("hospital.Hospital" ,
                                            through = "hospital.UserHospitalMembership" ,
                                            through_fields=("user", "hospital"),  # (source , target)
                                            )
    # Tip
    # Chon k ma mikhayeem yek through-model besazim va oon through-model ma az AuditTable ers bari mikone va oon ham chon khodesh
    # fk dare(created_by , updated_by) django nemifahme b kodom fk bayad point kone !Yani nimdone kodom field namayande rabeteh hastesh !
    # Ba through_fields serahatan moshakhas mikonim k django ba kodom field relation ro ijad kone (Add through_fields: The order is (source_field, target_field))

    
    USERNAME_FIELD  = "email" 
    REQUIRED_FIELDS = ["username"]

    objects         = CustomeUserManager()

    class Meta :
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        
    def __str__(self):

        return  self.email
    

    # Bayad Bebinam k ina chikar mikonn Hatman : !
    def has_perm(self, perm, obj=None): # todo?
        return self.is_superuser 

    def has_module_perms(self, app_label): # todo?
        return self.is_superuser and self.is_staff