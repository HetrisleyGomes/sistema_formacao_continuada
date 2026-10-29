from django.contrib import admin
from .models import Turma

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
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