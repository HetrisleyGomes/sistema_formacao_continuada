from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
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

    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Dados do sistema", {
            "fields": ("cpf", "perfil"),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Dados do sistema", {
            "classes": ("wide",),
            "fields": ("cpf", "perfil"),
        }),
    )

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser