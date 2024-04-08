from cadastro.serializers import (
    AlunoSerializer,
    AlunoSerializerBasic,
    ProfessorSerializer,
    ProfessorSerializerBasic,
)
from cadastro.models import Professor, Aluno
from erickgym.permissions import IsAdmin, IsAdminOrReadOnly, IsOwner, IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class ListAlunosAPIView(ReadOnlyModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializerBasic


class ListProfessoresAPIView(ReadOnlyModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializerBasic


class ListCreateAlunosAPIView(generics.ListCreateAPIView):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    permission_classes = [IsAdminOrReadOnly | IsOwnerOrReadOnly]

    def get(self, request):
        serializer = AlunoSerializerBasic(self.get_queryset(), many=True)
        return Response(serializer.data)


class RetrieveUpdateDestroyAlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    permission_classes = [IsAdmin | IsOwner]


class ListCreateProfessorAPIView(generics.ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    permission_classes = [IsAdminOrReadOnly]


class RetrieveUpdateDestroyProfessorAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    permission_classes = [IsAdmin | IsOwner]
