from django.urls import path, include
from cadastro.views import (
    ListCreateAlunosAPIView as CAlunosAPIView,
    RetrieveUpdateDestroyAlunoAPIView as RUDAlunoAPIView,
    ListCreateProfessorAPIView as CProfessoresAPIView,
    RetrieveUpdateDestroyProfessorAPIView as RUDProfessorAPIView,
)

app_name = "cadastro"


router_alunos = [
    path("alunos/", CAlunosAPIView.as_view(), name="list_create_aluno"),
    path(
        "alunos/<int:pk>/",
        RUDAlunoAPIView.as_view(),
        name="retrieve_update_destroy_aluno",
    ),
]

router_professores = [
    path("professores/", CProfessoresAPIView.as_view(), name="list_create_professor"),
    path(
        "profesores/<int:pk>",
        RUDProfessorAPIView.as_view(),
        name="retrive_update_destroy_professor",
    ),
]


routes = [*router_alunos, *router_professores]

urlpatterns = [
    path("cadastro/", include(routes)),
]
