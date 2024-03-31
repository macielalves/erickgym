from rest_framework import generics, permissions
from cadastro.serializers import AlunosSerializers
from cadastro.models import Alunos


class ListAlunosAPIView(generics.ListCreateAPIView):

    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializers

    permission_classes = [permissions.IsAuthenticated]


class ListAlunoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializers
    permission_classes = [permissions.IsAuthenticated]
