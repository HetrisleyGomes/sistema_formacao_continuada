from django.core.exceptions import ValidationError

def validar_cpf(valor):
    cpf = "".join(filter(str.isdigit, str(valor)))

    if len(cpf) != 11:
        raise ValidationError("O CPF deve ter 11 números.")

    if cpf == cpf[0]*11:
        raise ValidationError("Informe um CPF válido.")

    soma = sum(int(cpf[i]) * (10-i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    if digito1 != int(cpf[9]):
        raise ValidationError("Informe um CPF válido.")

    soma = sum(int(cpf[i]) * (11-i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    if digito2 != int(cpf[10]):
        raise ValidationError("Informe um CPF válido.")