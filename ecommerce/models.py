from django.db import models
from . import validators
import datetime
from django.core.validators import MinLengthValidator


class Usuario(models.Model):
    name = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11, unique=True,
                           validators=[validators.valida_cpf, MinLengthValidator(11)])

    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Produto(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pedido(models.Model):
    total = models.FloatField()
    invoice_date = models.DateField(default=datetime.date.today)
    products = models.ManyToManyField(Produto)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
