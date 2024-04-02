from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, date_of_birth=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        if not date_of_birth:
            raise ValueError('Users must have a date of birth')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            date_of_birth=date_of_birth
        )

        user.set_password(password)  # Set password hash, not plain text
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, date_of_birth=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
