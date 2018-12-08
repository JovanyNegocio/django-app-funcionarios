from django.db import models

# Create your models here.

class Funcionario(models.Model):

    nome = models.CharField(max_length=250, null=False, blank=False)

    sobrenome = models.CharField(max_length=250, null=False, blank=False)

    bilhete = models.CharField(max_length=14, null=False, blank=False)

    tempo_de_servico = models.IntegerField(default=0, null=False, blank=False)

    salario = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    objetos = models.Manager()
