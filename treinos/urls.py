from django.urls import path
from .views import (
    ListCreateExercicioAPIView as ExerciciosAPIView,
    DetailUpdateDeleteExercicio as ExercicioAPIView,
)


urlpatterns = [
    path("<int:pk>", ExercicioAPIView.as_view(), name="exercicio"),
    path("", ExerciciosAPIView.as_view(), name="exercicios"),
]
