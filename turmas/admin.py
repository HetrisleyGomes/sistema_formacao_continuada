from django.contrib import admin
from usuarios.admin_mixins import AcessoGestoresAdmin
from .models import Turma

@admin.register(Turma)
class TurmaAdmin(AcessoGestoresAdmin):
    list_display = (
        "nome",
        "formacao",
        "data_inicio",
        "data_fim",
        "ativa",
    )

    search_fields = (
        "nome",
        "formacao__titulo",
    )

    list_filter = (
        "ativa",
        "data_inicio",
        "formacao",
    )

    date_hierarchy = "data_inicio"