from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='passport')
    role = models.CharField(max_length=10)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)
    reset_password = models.BooleanField(default=False)
    ref = models.UUIDField(default=uuid4)