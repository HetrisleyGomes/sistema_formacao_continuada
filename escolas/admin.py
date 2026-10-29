from django.contrib import admin
from .models import Escola

@admin.register(Escola)
class EscolaAdmin(admin.ModelAdmin):
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
