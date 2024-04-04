from django.urls import path
from .views import (
    ListCreateAlunosAPIView,
    RetrieveUpdateDestryAlunoAPIView,
    ListCreateProfessor,
    RetrieveUpdateDestroyProfessor,
)

alunos_urls = [
    path("<int:pk>", RetrieveUpdateDestryAlunoAPIView.as_view(), name="aluno"),
    path("", ListCreateAlunosAPIView.as_view(), name="alunos"),
]

professores_urls = [
    path("<int:pk>", RetrieveUpdateDestroyProfessor.as_view(), name="professor"),
    path("", ListCreateProfessor.as_view(), name="professores"),
]
