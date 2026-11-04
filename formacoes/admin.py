from django.contrib import admin
from usuarios.admin_mixins import AcessoGestoresAdmin
from .models import Formacao

@admin.register(Formacao)
class FormacaoAdmin(AcessoGestoresAdmin):
    list_display = (
        "titulo",
        "tema",
        "carga_horaria",
        "ativa",
    )

    search_fields = ("titulo", "tema")

    list_filter = ("ativa",)