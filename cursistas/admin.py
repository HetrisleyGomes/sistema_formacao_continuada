from django.contrib import admin
from usuarios.admin_mixins import AcessoGestoresAdmin
from .models import Cursista

@admin.register(Cursista)
class CursistaAdmin(AcessoGestoresAdmin):
    list_display = (
        "nome_completo",
        "cpf",
        "funcao",
        "escola",
        "ativo",
    )

    search_fields = (
        "nome_completo",
        "cpf",
    )

    list_filter = (
        "funcao",
        "escola",
        "ativo",
    )
