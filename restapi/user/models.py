from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import CustomUserManager

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
 
    username = models.CharField(max_length=20, unique=True, null=False)
    email = models.EmailField(max_length=60, unique=True, null=True)
    usertype = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = CustomUserManager()


    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True