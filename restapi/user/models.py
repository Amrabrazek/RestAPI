from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    
    USERNAME_FIELD = 'username'

    TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('customer', 'Customer')
    ]
    GENDER_CHOICES = [
        ('m', 'Male'),
        ('f', 'Female'),
        ('notsay', 'Prefer Not to say')
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=60, unique=True, null=True)
    usertype = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    activated = models.BooleanField(default=False, null=True)

