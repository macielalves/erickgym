from cadastro.models import Aluno, Professor
from django.contrib import admin


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["nome"]


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ["nome", "area_de_atuação"]
