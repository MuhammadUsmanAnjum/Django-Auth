from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150,
        unique=True,
        null=True,
        blank=True
       
    )
    email_token = models.CharField(max_length=36, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username']


