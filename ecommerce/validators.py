from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valida_cpf(value):
    value = str(value).zfill(11)
    if not value.isnumeric():
        raise ValidationError(
            _('CPF deve conter apenas números. (Valor informado:%(oldvalue)s)'),
            params={'value': value},
        )
