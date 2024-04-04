from django.db import models


class Base(models.Model):
    SEXO_CHOICE = (
        ("M", "Masculino"),
        ("F", "Femenino"),
    )
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to="img/")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        abstract = True


class Alunos(Base):
    foto = models.ImageField(upload_to="img/alunos", blank=True, null=True)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"


class Professor(Base):
    foto = models.ImageField(upload_to="img/professores")
    area_de_atuação = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Professores"
