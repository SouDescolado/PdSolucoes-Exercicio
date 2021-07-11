from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valida_cpf(value):
    if not value.isnumeric():
        raise ValidationError(
            _('CPF deve conter apenas números. (Valor informado:%(value)s)'),
            params={'value': value},
        )
