from django.urls import path
from . import views

app_name = "relatorios"

urlpatterns = [
    path(
        "participantes/",
        views.relatorio_participantes,
        name="participantes",
    ),
    path(
        "participantes/excel/",
        views.export_participantes_excel,
        name="participantes_excel",
    ),
    path(
        "participantes/pdf/",
        views.export_participantes_pdf,
        name="participantes_pdf",
    ),
    path(
        "consolidado/",
        views.relatorio_consolidado,
        name="consolidado",
    ),
    path(
        "consolidado/excel/",
        views.export_consolidado_excel,
        name="consolidado_excel",
    ),
    path(
        "consolidado/pdf",
        views.export_consolidado_pdf,
        name="consolidado_pdf"
    ),
]