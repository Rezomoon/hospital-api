from django.db import models

# Create your models here.


class Role(models.Model) : 
    name        = models.CharField(max_length=150 , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    def __str__(self):
        return self.name
class Status(models.Model) :
    name        = models.CharField(max_length=150 , null=True , blank=True)
    description = models.TextField(null=True , blank=True)
    def __str__(self):
        return self.name