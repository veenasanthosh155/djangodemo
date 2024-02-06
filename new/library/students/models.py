from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    place= models.TextField(default="")
    def __str__(self):
        return self.username
