from django.db import models

class Formacao(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name="Título da formação"
    )
    tema = models.CharField(
        max_length=200,
        verbose_name="Tema"
    )
    descricao = models.TextField(
        blank=True,
        verbose_name="Descrição"
    )
    carga_horaria = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Carga horária total (horas)"
    )
    ativa = models.BooleanField(
        default=True,
        verbose_name="Formação ativa"
    )
    criada_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de cadastro"
    )
    class Meta:
        verbose_name = "Formação"
        verbose_name_plural = "Formações"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo