import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class SimpleUserManager(UserManager):
    def create_user(self, username, **extra_fields):
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.is_active = False
        user.is_staff = False
        user.set_password(make_password(password=None))
        user.save(using=self._db)
        print("CREATE USER", extra_fields)
        return user

    def create_superuser(self, username, password, **extra_fields):
        # email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        print("CREATE SUPERUSER", extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = SimpleUserManager()

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name

    def __str__(self):
        return self.username


# python manage.py migrate admin zero
# python manage.py migrate auth zero
# python manage.py migrate contenttypes zero
# python manage.py migrate sessions zero
