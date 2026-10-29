from django.contrib import admin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "cpf",
        "email",
        "perfil",
        "is_active",
    )

    search_fields = (
        "username",
        "cpf",
        "email",
        "first_name",
        "last_name",
    )

    list_filter =(
        "perfil",
        "is_active",
    )