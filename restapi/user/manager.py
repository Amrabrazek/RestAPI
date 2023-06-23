
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, usertype, gender, is_active, password=None):
        if not email:
            raise ValueError('User must have an email')
        
        user = self.model(email=self.normalize_email(email), username=username, usertype=usertype, gender=gender, is_active=is_active)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, email, username, password=None):
        user = self.create_user(username, email, 'admin', 'm', True, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user