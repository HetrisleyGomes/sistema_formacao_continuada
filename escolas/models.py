from django.db import models

class Escola(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome da escola"
    )
    codigo_inep = models.CharField(
        max_length=8,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Código INEP"
    )
    ativa = models.BooleanField(
        default=True,
        verbose_name="Escola ativa"
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )
    def __str__(self):
        return self.nome
