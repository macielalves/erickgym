from django.db import models
from django.contrib.auth.models import User


class Exercicio(models.Model):
    nome = models.CharField(max_length=250, unique=True)
    descricao = models.CharField(max_length=500)
    ativo = models.BooleanField(default=True)
    idade_minima_aluno = models.PositiveIntegerField(default=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f"{self.nome} - {self.user.get_short_name()} - {self.ativo}"
