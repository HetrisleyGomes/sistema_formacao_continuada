from django.core.exceptions import ValidationError
from django.db import models

from cursistas.models import Cursista
from turmas.models import Turma

class Inscricao(models.Model):
    class Situacao(models.TextChoices):
        ATIVA = "ATIVA", "Ativa"
        CANCELADA = "CANCELADA", "Cancelda"

    cursista = models.ForeignKey(
        Cursista,
        on_delete=models.PROTECT,
        related_name="inscricoes",
        verbose_name="Cursista"
    )
    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        related_name="inscricoes",
        verbose_name="Turma"
    )
    data_inscricao = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de inscrição"
    )
    situacao = models.CharField(
        max_length=10,
        choices=Situacao.choices,
        default=Situacao.ATIVA,
        verbose_name="Situação"
    )

    class Meta:
        verbose_name = "Inscrição",
        verbose_name_plural = "Inscrições"
        ordering = ["-data_inscricao"]

        constraints = [
            models.UniqueConstraint(
                fields=["cursista", "turma"],
                name="inscricao_unica_por_cursista_turma"
            )
        ]

    def clean(self):
        super().clean()

        if self.cursista_id and self.turma_id:
            inscricao_existente = Inscricao.objects.filter(
                cursista_id=self.cursista_id,
                turma__formacao_id=self.turma.formacao_id,
            ).exclude(pk=self.pk)

            if inscricao_existente.exists():
                raise ValidationError({
                    "turma": ("Este cursista já possui uma inscrição em outra turma desta formação.")
                })

    def __str__(self):
        return f"{self.cursista} - {self.turma}"