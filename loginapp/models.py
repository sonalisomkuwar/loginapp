from django.db import models

# Create your models here.

        
class login(models.Model):
    user_name=models.CharField(max_length=150)
    password=models.CharField(max_length=250)
