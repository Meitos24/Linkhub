from django.db import models # type: ignore

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    rol = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)