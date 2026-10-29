from django.contrib import admin
from .models import Encontro

@admin.register(Encontro)
class EncontroAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "turma",
        "data",
        "carga_horaria",
        "situacao",
    )

    search_fields = (
        "titulo",
        "turma__nome",
        "turma__formacao__titulo",
    )

    list_filter = (
        "situacao",
        "data",
        "turma",
    )

    date_hierarchy = "data"

    autocomplete_fields = ("turma",)
