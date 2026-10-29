from django.contrib import admin
from .models import Inscricao
from .services import calcular_frequencia

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = (
        "cursista",
        "turma",
        "data_inscricao",
        "situacao",
        "horas_frequentadas",
        "percentual_frequencia",
        "resultado_conclusao",
    )

    search_fields = (
        "cursista__nome_completo",
        "cursista__cpf",
        "turma__nome",
        "turma__formacao__titulo",
    )

    list_filter = (
        "situacao",
        "turma",
        "data_inscricao",
    )

    autocomplete_fields = ("cursista", "turma")

    @admin.display(description="Horas frequentadas")
    def horas_frequentadas(self, obj):
        resultado = calcular_frequencia(obj)
        return resultado["horas_frequentadas"]

    @admin.display(description="Frequencia (%)")
    def percentual_frequencia(self, obj):
        resultado = calcular_frequencia(obj)
        return f'{resultado["percentual_frequencia"]}%'

    @admin.display(description="Conclusão")
    def resultado_conclusao(self, obj):
        resultado = calcular_frequencia(obj)
        if resultado["horas_realizadas"] == 0:
            return "Sem encontros realizados"
        if resultado["concluinte"]:
            return "Conluinte"
        return "Não concluinte"
