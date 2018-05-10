from django.db import models

# Create your models here.
#from django.contrib.auth.models import 

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
#from datetime import datetime
from django.utils import timezone as timezone
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,username,password=None,dada=None, **kwargs):
        # Ensure that an email address is set
       
        if not email:
            raise ValueError('Users must have a valid e-mail address')
        # Ensure that a username is set
      
        user = self.model(
            email=self.normalize_email(email),
            username=username
           # enrichjson= enrichjson,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        
        #username = kwargs.get('username')
        user = self.create_user(email, username,password, kwargs)
        #user.is_admin = True
        user.is_staff = True
        user.is_superuser = True 
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=60)
    email = models.EmailField(unique=True) 
    is_active = models.BooleanField(default=True)
    #is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']