from django.db import models

# Create your models here.
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')
        # Ensure that a username is set
        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username')
        user = self.model(
            email=self.normalize_email(email),
            username=kwargs.get('username'),
           # enrichjson= enrichjson,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, kwargs)
        user.is_admin = True
        user.save()

        return user

class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=60)
    email = models.EmailField(unique=True) 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now())
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']