from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser):
    phone = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    howDidYouFindUs = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)
    # Add other fields as necessary

    class Meta:
        db_table = 'users'  # Specify the existing table name


class ContactUs(AbstractBaseUser):
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    fullName = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    # Add other fields as necessary

    class Meta:
        db_table = 'contactus'  # Specify the existing table name