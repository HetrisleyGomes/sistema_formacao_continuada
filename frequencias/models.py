from django.core.exceptions import ValidationError
from django.db import models

from inscricoes.models import Inscricao
from encontros.models import Encontro

class Frequencia(models.Model):
    inscricao = models.ForeignKey(
        Inscricao,
        on_delete=models.PROTECT,
        related_name="frequencias",
        verbose_name="Inscrição"
    )
    encontro = models.ForeignKey(
        Encontro,
        on_delete=models.PROTECT,
        related_name="frequencias",
        verbose_name="Encontro"
    )
    presente = models.BooleanField(
        null=True,
        blank=True,
        default=None,
        verbose_name="Presente"
    )
    observacao = models.TextField(
        blank=True,
        verbose_name="Observação"
    )
    registrado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Última atualização"
    )

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"
        ordering = [
            "encontro__data",
            "inscricao__cursista__nome_completo"
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["inscricao", "encontro"],
                name="frequencia_unica_por_inscricao_encontro"
            )
        ]

    def clean(self):
        super().clean()

        if self.inscricao_id and self.encontro_id:
            if self.inscricao.turma_id != self.encontro.turma_id:
                raise ValidationError({
                    "encontro": ("O encontro selecionado não pertence à turma desta inscrição.")
                })

    def __str__(self):
        return (
            f"{self.inscricao.cursista} - {self.encontro.titulo}"
        )