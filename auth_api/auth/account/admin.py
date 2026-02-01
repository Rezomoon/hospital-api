from django.contrib import admin
from .models import BaseCustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import Role
# Register your models here. 


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
                        "role" ,
                        "status",)
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
             "fields"           : (("is_admin", "is_staff", "is_superuser",),"role","status") ,
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

    list_display = ("id", "username", "email",  "full_name", "is_staff", "is_admin","person_code" ,"get_status", "get_role" )


    def get_role(self , obj ) :
        return [role.name for role in obj.role.all()]
    get_role.short_description = "Role"
    def get_status(self, obj) : 
        return [status.name  for status in obj.status.all()]
    get_status.short_description = "Status"
    list_filter = ("is_staff", "is_superuser", "is_active", ) #"groups" todo
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username","is_superuser")
    filter_horizontal = (
       # "groups", todo
       # "user_permissions", todo
    )
   
class RoleModelAdmin(admin.ModelAdmin) :
    list_display = ["id" , "name", "description"]
admin.site.register(Role, RoleModelAdmin)