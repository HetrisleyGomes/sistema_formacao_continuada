from django.contrib import admin
from .models import Formacao

@admin.register(Formacao)
class FormacaoAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "tema",
        "carga_horaria",
        "ativa",
    )

    search_fields = ("titulo", "tema")

    list_filter = ("ativa",)