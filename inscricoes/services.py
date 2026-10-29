from decimal import Decimal
from django.db.models import Sum

from encontros.models import Encontro
from frequencias.models import Frequencia
from .models import Inscricao

PERCENTUAL_MINIMO_CONCLUSAO = Decimal("75.00")

def calcular_frequencia(inscricao: Inscricao) -> dict:
    encontros_realizados = Encontro.objects.filter(
        turma_id=inscricao.turma_id,
        situacao=Encontro.Situacao.REALIZADO
    )

    resultado_total = encontros_realizados.aggregate(
        total=Sum("carga_horaria")
    )

    horas_realizadas = (
        resultado_total["total"] or Decimal("0.00")
    )

    resultado_presenca = Frequencia.objects.filter(
        inscricao=inscricao,
        encontro__in=encontros_realizados,
        presente=True
    ).aggregate(
        total=Sum("encontro__carga_horaria")
    )

    horas_frequentadas = (
        resultado_presenca["total"] or Decimal("0.00")
    )

    if horas_realizadas > 0:
        percentual = (
            horas_frequentadas / horas_realizadas
        ) * Decimal("100")

        percentual = percentual.quantize(Decimal("0.01"))
    else:
        percentual = Decimal("0.00")

    concluinte = (
        horas_realizadas > 0
        and percentual >= PERCENTUAL_MINIMO_CONCLUSAO
    )

    return {
        "horas_realizadas": horas_realizadas,
        "horas_frequentadas": horas_frequentadas,
        "percentual_frequencia": percentual,
        "concluinte": concluinte,
    }