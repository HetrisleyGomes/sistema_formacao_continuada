from django.contrib import admin
from usuarios.admin_mixins import AcessoGestoresAdmin
from .models import Escola

@admin.register(Escola)
class EscolaAdmin(AcessoGestoresAdmin):
    list_display = (
        "nome",
        "codigo_inep",
        "ativa",
    )
    search_fields = (
        "nome",
        "codigo_inep",
    )

    list_filter = (
        "ativa",
    )
