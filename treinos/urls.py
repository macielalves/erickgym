from django.urls import path
from .views import ListaExerciciosAPIView, ExercicioAPIView


urlpatterns = [
    path("exercicios/<int:pk>", ExercicioAPIView.as_view(), name="exercicio"),
    path("exercicios/", ListaExerciciosAPIView.as_view(), name="exercicios"),
]
