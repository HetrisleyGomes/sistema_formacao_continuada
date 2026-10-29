from django.contrib import admin
from .models import Cursista

@admin.register(Cursista)
class CursistaAdmin(admin.ModelAdmin):
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
