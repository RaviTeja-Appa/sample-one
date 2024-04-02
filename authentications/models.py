from django.db import models

# Create your models here.
# Use PermissionsMixin for Django >= 2.0
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Inherit from PermissionsMixin for Django >= 2.0
class User(AbstractBaseUser, PermissionsMixin):

    user_image = models.ImageField(blank=True, upload_to='userimages/')

    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_of_birth = models.DateField(blank=False, null=False)  # Make required
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'date_of_birth']

    def __str__(self):
        return self.email
