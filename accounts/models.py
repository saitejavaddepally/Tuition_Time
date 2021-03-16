from django.db import models

# Create your models here.

class user_register(models.Model):
     first_name = models.CharField(max_length=20)
     last_name = models.CharField(max_length=20)
     user_name = models.CharField(max_length=20)
     email = models.CharField(max_length=100)
     password = models.CharField(max_length=256)
     

# class user_login(models.Model):
#      email_auth = models.CharField(max_length=100)
#      passwod_auth = models.CharField(max_length=20)  