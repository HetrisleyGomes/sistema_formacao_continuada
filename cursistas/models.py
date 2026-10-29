from django.db import models
from escolas.models import Escola

class Cursista(models.Model):
    class Funcao(models.TextChoices):
        PROFESSOR = "PROFESSOR", "Professor"
        COORDENADOR = "COORDENADOR", "Coordenador pedagógico"
        DIRETOR = "DIRETOR", "Diretor"

    nome_completo = models.CharField(
        max_length=200,
        verbose_name="Nome Completo"
    )
    cpf = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="CPF"
    )
    contato = models.CharField(
        max_length=100,
        verbose_name="Contato"
    )
    escola = models.ForeignKey(
        Escola,
        on_delete=models.PROTECT,
        related_name='cursistas',
        verbose_name='Escola'
    )
    funcao = models.CharField(
        max_length=20,
        choices=Funcao.choices,
        verbose_name="Função"
    )
    ativo = models.BooleanField(
        default=True,
        verbose_name="Cursista ativo"
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )
    class Meta:
        verbose_name = "Cursista"
        verbose_name_plural = "Cursistas"
        ordering = ["nome_completo"]

    def __str__(self):
        return self.nome_completo