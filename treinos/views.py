# from rest_framework.views import APIView
from rest_framework import generics, permissions
from treinos.serializers import ExercicioSerializer
from treinos.models import Exercicio


# CBV --> Class Based View
class ListaExerciciosAPIView(generics.ListCreateAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer

    permission_classes = [permissions.IsAuthenticated]


class ExercicioAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer

    permission_classes = [permissions.IsAuthenticated]


# class ListaExerciciosView(APIView):

#     def get(self, request):
#         exercicios = Exercicio.objects.all()
#         serializer = ExercicioSerializer(exercicios, many=True)
#         return Response(serializer.data, status=200)

#     def post(self, request):
#         serializer = ExercicioSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)

#     def put(self, request, pk):  # Preferível usar put ao invés de patch
#         exercicio = get_object_or_404(pk)
#         serializer = ExercicioSerializer(exercicio, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)

#     def delete(self, request, pk):
#         exercicio = get_object_or_404(pk)
#         exercicio.delete()
#         return Response({"message": "Exercício excluído"}, status=204)
