from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, default=False)
    email = models.EmailField(unique=True)
    
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email