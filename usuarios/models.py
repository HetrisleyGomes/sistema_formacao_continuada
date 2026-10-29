from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    cpf = models.CharField(
        max_length=11, unique=True, verbose_name="CPF"
    )

    class Perfil(models.TextChoices):
        ADMINISTRADOR = "ADMIN", "Administrador"
        GESTOR = "GESTOR", "Gestor de formação"
        CURSISTA = "CURSISTA", "Cursista"

    perfil = models.CharField(
        max_length=10, choices=Perfil.choices, default=Perfil.CURSISTA, verbose_name="Perfil"
    )

    def __str__(self):
        return self.get_full_name()