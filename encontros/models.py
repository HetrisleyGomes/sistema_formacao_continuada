from decimal import Decimal
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Q
from turmas.models import Turma

class Encontro(models.Model):
    class Situacao(models.TextChoices):
        AGENDADO = "AGENDADO", "Agendado"
        REALIZADO = "REALIZADO", "Realizado"
        CANCELADO = "CANCELADO", "Cancelado"

    turma = models.ForeignKey(
        Turma,
        on_delete=models.PROTECT,
        related_name="encontros",
        verbose_name="Turma"
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name="Titulo do encontro"
    )
    data = models.DateField(
        verbose_name="Data do encontro"
    )
    carga_horaria = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
        verbose_name="Carga horária do encontro (horas)"
    )
    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição"
    )
    situacao= models.CharField(
        max_length=10,
        choices=Situacao.choices,
        default=Situacao.AGENDADO,
        verbose_name="Situação"
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )

    def clean(self):
        super().clean()
        if self.turma_id and self.data:
            turma = self.turma
            if self.data < turma.data_inicio:
                raise ValidationError({
                    "data": "A data do encontro não pode ser anterior ao início da turma."
                })
            if turma.data_fim and self.data > turma.data_fim:
                raise ValidationError({
                    "data": "A data do encontro não pode ser posterior ao encerramento da turma."
                })

    class Meta:
        verbose_name = "Encontro"
        verbose_name_plural = "Encontros"
        ordering = ["data","titulo"]

    def __str__(self):
        return f"{self.titulo} - {self.data:%d/%m/%Y}"