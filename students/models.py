from django.db import models

class register(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    phone=models.CharField(max_length=13)
    mail=models.CharField(max_length=50)
 

# Create your models here.
