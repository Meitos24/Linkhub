from django.db import models # type: ignore

# Create your models here.

class RoleChoices(models.TextChoices):
    ADMIN = "admin", "Administrador Global"  # Admin de la plataforma
    COMPANY_ADMIN = (
        "company_admin",
        "Administrador de Empresa"
    )  # Admin para su propia empresa
    TECH = "tech", "Técnico"  # Usuario que opera/ejecuta
    VIEWER = "viewer", "Visualizador"  # Solo lectura
class Usuario(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    rol = models.CharField(
        max_length=30,
        choices=RoleChoices.choices,
        default=RoleChoices.VIEWER
    )
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.username})"