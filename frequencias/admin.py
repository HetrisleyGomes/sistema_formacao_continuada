from django.contrib import admin
from usuarios.admin_mixins import AcessoGestoresAdmin
from .models import Frequencia

@admin.register(Frequencia)
class FrequenciaAdmin(AcessoGestoresAdmin):
    list_display = (
        "inscricao",
        "encontro",
        "presente",
        "registrado_em",
    )

    search_fields = (
        "inscricao__cursista__nome_completo",
        "inscricao__cursista__cpf",
        "encontro__titulo",
        "encontro__turma__nome",
    )

    list_filter = (
        "presente",
        "encontro__data",
        "encontro__turma",
    )

    autocomplete_fields = ("inscricao", "encontro")
