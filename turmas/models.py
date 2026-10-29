from django.db import models
from formacoes.models import Formacao

class Turma(models.Model):
    formacao = models.ForeignKey(
        Formacao,
        on_delete=models.PROTECT,
        related_name="turmas",
        verbose_name="Formação"
    )
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome da turma"
    )
    data_inicio = models.DateField(
        verbose_name="Data de início"
    )
    data_fim = models.DateField(
        null=True,
        blank=True,
        verbose_name="Data de encerramento"
    )
    local = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Local de realização"
    )
    ativa = models.BooleanField(
        default=True,
        verbose_name="Turma ativa"
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )
    class Meta:
        verbose_name="Turma"
        verbose_name_plural = "Turmas"
        ordering = ["-data_inicio", "nome"]

    def __str__(self):
        return f"{self.nome} - {self.formacao.titulo}"