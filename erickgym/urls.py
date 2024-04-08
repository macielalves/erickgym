from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from erickgym.views import UserViewSet
from rest_framework import routers
from django.contrib import admin
from cadastro.views import ListAlunosAPIView, ListProfessoresAPIView
from treinos.views import ListExerciciosAPIView

# Routers ViewSets
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"api/r/alunos", ListAlunosAPIView)
router.register(r"api/r/professores", ListProfessoresAPIView)
router.register(r"api/r/exercicios", ListExerciciosAPIView)

urlpatterns = [
    path("", include(router.urls)),
    path("api/", include("cadastro.urls"), name="cadastro"),
    path("api/", include("treinos.urls"), name="treinos"),
    path("admin/", admin.site.urls),
    path("api/auth/", include("rest_framework.urls")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
