from rest_framework import generics, authentication
from cadastro.serializers import AlunosSerializers, ProfessoresSerializers
from cadastro.models import Alunos, Professor
from erickgym.permissions import IsAdmin, IsAdminOrReadOnly, IsOwner


class ListCreateAlunosAPIView(generics.ListCreateAPIView):

    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializers

    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]


class RetrieveUpdateDestryAlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializers

    permission_classes = [IsAdmin | IsOwner]

    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]


class ListCreateProfessor(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessoresSerializers

    permission_classes = [IsAdminOrReadOnly]

    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]


class RetrieveUpdateDestroyProfessor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessoresSerializers

    permission_classes = [IsAdmin | IsOwner]

    authentication_classes = [
        authentication.TokenAuthentication,
        authentication.SessionAuthentication,
    ]
