from django.contrib import admin
from .models import Usuario

class AcessoGestoresAdmin(admin.ModelAdmin):
    def usuario_pode_gerenciar(self,request):
        user = request.user
        return (
            user.is_authenticated
            and user.is_active
            and (
                user.is_superuser
                or user.perfil in (
                    Usuario.Perfil.ADMINISTRADOR,
                    Usuario.Perfil.GESTOR,
                )
            )
        )

    def has_module_permission(self, request):
        return self.usuario_pode_gerenciar(request)

    def has_view_permission(self, request, obj=None):
        return self.usuario_pode_gerenciar(request)

    def has_add_permission(self, request):
        return self.usuario_pode_gerenciar(request)

    def has_change_permission(self, request, obj=None):
        return self.usuario_pode_gerenciar(request)

    def has_delete_permission(self, request, obj=None):
        return self.usuario_pode_gerenciar(request)