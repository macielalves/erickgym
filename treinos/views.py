from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from treinos.serializers import ExercicioSerializer, ExercicioSerializerToRead
from treinos.models import Exercicio
from erickgym.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class ListCreateExercicioAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        exercicios = get_list_or_404(Exercicio)
        serialize = ExercicioSerializer(exercicios, many=True)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ExercicioSerializer(data={"user": request.user.id, **request.data})
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"details": "Exercício registrado com sucesso!"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailUpdateDeleteExercicio(APIView):
    permission_classes = [IsOwnerOrReadOnly | IsAdminOrReadOnly]

    def get(self, request, pk, format=None):
        """Retorna um exericio específico"""
        exercicio = get_object_or_404(Exercicio, id=pk)
        serializer = ExercicioSerializer(exercicio)
        return Response(serializer.data)

    def put(self, request, pk):
        exercicio = get_object_or_404(Exercicio, id=pk)
        serializer = ExercicioSerializer(exercicio, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        exercicio = get_object_or_404(Exercicio, id=pk)
        exercicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListExerciciosAPIView(ReadOnlyModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializerToRead
