from django.shortcuts import render
from usuarios.decorators import gestor_ou_administrador_required

@gestor_ou_administrador_required
def inicio(request):
    return render(request, "painel/inicio.html")