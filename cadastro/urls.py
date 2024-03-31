from django.urls import path
from .views import ListAlunosAPIView, ListAlunoAPIView


urlpatterns = [
    path("alunos/<int:pk>", ListAlunoAPIView.as_view(), name="aluno"),
    path("alunos/", ListAlunosAPIView.as_view(), name="alunos"),
]
