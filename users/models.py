from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username
