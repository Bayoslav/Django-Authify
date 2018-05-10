#### Django-Authy 

Django-Authy is a VERY lightweight authentication app for Django 2.0.
It extends the Django AbstractBaseUser and BaseUserManager for the new User class.

If you have any problems with using this just open an issue here and I'll respond asap. 


##### Install instructions 

   1. Add 'authentication' to your installed apps in settings.py
   
   1a. Add this to your settings.py:
   ```
   AUTH_USER_MODEL = 'authentication.User'
   ```
   2. Add the user model to the database
   
    
    python manage.py makemigrations
    python manage.py migrate
   
    
