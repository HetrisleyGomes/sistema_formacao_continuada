from django.contrib.auth.decorators import user_passes_test

from .models import Usuario

def gestor_ou_administrador_required(view_func):
    def usuario_autorizado(user):
        return (
            user.is_authenticated
            and user.is_active
            and user.perfil in (
                Usuario.Perfil.ADMINISTRADOR,
                Usuario.Perfil.GESTOR,
            )
        )
    return user_passes_test(
        usuario_autorizado,
        login_url="admin:login",
    )(view_func)