from django.db import models


class Exercicio(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=500)
    ativo = models.BooleanField(default=True)
    idade_minima_aluno = models.PositiveIntegerField(default=12)
