from django.db import models

# Create Your Constants : 

class GenderChoices(models.TextChoices) : 
    Male = "Male"
    Femail = "Female"
    