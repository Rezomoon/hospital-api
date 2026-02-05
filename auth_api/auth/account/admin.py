from django.contrib import admin
from .models import BaseCustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import Role , Status
from django.contrib.auth import get_user_model
# Register your models here. 



class CustomUserInLine(admin.TabularInline) : 
    """
    Cuase We Have manyTomany Field and through table we use this way
    """
    model   = get_user_model().hospital.through
    fk_name = "user"


@admin.register(BaseCustomUser)
class BaseCustomUserAdminModel(UserAdmin) :
    """
    Docstring for BaseCustomUserAdminModel
    Tips : In Class az roye Class UserAdmin Khode Django Olgo Bardari shode va yek seri chiz ha kam dare (django.contrib.aut.admin import UserAdmin)

    Todo :
        form = UserChangeForm ?
        add_form = UserCreationForm ? 
        change_password_form = AdminPasswordChangeForm ?

    Bug : agar az admin.ModelAdmin estefadeh konim : When Add User In Django Admin Password Is Not Hash! todo
    """

    fieldsets = (
        (
            "اضافه کردن اطلاعات کاربری", 
        {   
            "description"    : " نام کاربری و ایمیل نباید تکراری باشند !" ,
            "classes"       : ("wide" ,) ,
            "fields"        : ("email","username" , "password"),
            
            },
            
        )  ,

        (
            "اطلاعات شخصی" ,  
        {   
            "description"   : "اطلاعات تکمیلی و اختیاری :" ,
            "classes"       : ("collapse",) , 
            "fields" : ("first_name", "last_name", "date_of_birth",("weight" , "height") ) ,
        }    
         ) ,

        (
            "نفش ها و دسترسی ها" , 
            
            {
                "description"   : "تنظیمات دسترسی ها و نقش های کاربر " ,
                "classes"       : ("wide" ,) ,
                "fields" : (
                        "is_active" , 
                        "is_staff",
                        "is_superuser",
                        "is_admin" ,
                        # "role" ,
                        "status",
                        # "departement",
                        ) 
                        }
        ) ,


        ("اطلاعات سیستمی", 
         {
            "classes"       : ("collapse" ,) ,
            "fields" :("last_login", ) , 
            }
             )
        
    )

    add_fieldsets = ( #todo?
        (
            "ساختن یک کاربر جدید",
            {
                "classes"       : ("wide",),
                "fields"        : ("email", "username", "password1", "password2" , ),
                "description"   : "نام کاربری و ایمیل نباید تکراری باشند"
            },
        ),
        (
            "دسترسی ها و نقش ها" ,
         {
             "classes"          :  ["wide",],
             "fields"           : (("is_admin", "is_staff","is_superuser",),
                                #    "role",
                                   "status" ,
                                #    "departement" ,
                                    ) ,
             "description"      : "تنظیمات دسترسی ها و نقش های کاربر"
         }
         ),
         (
            "اطلاعات شخصی کاربر" , 
            {
                "classes"   : ("collapse",) ,
                "fields"    : ("first_name", "last_name","date_of_birth" , ("weight" , "height")) , 
                "description"   : "اطلاعات تکمیلی و اختیاری :"
            }
         ),
    )

    list_display = ("id", "username",
                    "email",  "full_name",
                    "is_staff", "is_admin",
                    "person_code" ,
                    "status",
                    # "get_role",
                    "get_hospital" ,
                    # "get_departement" ,
                          ) # 


    # def get_role(self , obj ) :
    #     return [role.name for role in obj.role.all()]

    # get_role.short_description = "Role"

    def get_hospital(self , obj) :
        return [hospital.name for hospital in obj.hospital.all()]
    get_hospital.short_description = "Hospital"

    # def get_departement(self , obj) : 
    #     return [departement.name for departement in obj.departement.all()]
    # get_departement.short_description = "Departement"

    
    list_filter     = ("is_staff", "is_superuser", "is_active", ) #"groups" todo
    search_fields   = ("username", "first_name", "last_name", "email")
    ordering        = ("username","is_superuser")
    inlines         = [CustomUserInLine]
    filter_horizontal = (
    #    "groups",      #todo
    # "user_permissions", todo
    )
   
class RoleModelAdmin(admin.ModelAdmin) :
    list_display = ["id" , "name", "description"]
admin.site.register(Role, RoleModelAdmin)


class StatusModelAdmin(admin.ModelAdmin) :
    list_display = ["id" , "name", "description"]
admin.site.register(Status , StatusModelAdmin)