from django.db import models


SEXO_CHOICE = (
    ("M", "Masculino"),
    ("F", "Femenino"),
)


class Base(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="img/")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)

    class Meta:
        abstract = True


class Alunos(Base):
    foto = models.ImageField(upload_to="img/alunos", blank=True, null=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.nome
