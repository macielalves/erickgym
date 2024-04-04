from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from erickgym.views import login, singup, UserViewSet, test_token
from cadastro.urls import (
    alunos_urls,
    professores_urls,
)
from rest_framework import routers


# Routers ViewSets
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/alunos/", include(alunos_urls)),
    path("api/professores/", include(professores_urls)),
    path("api/exercicios/", include("treinos.urls")),
    path("api/auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path("login/", login, name="entrar"),
    re_path("singup/", singup, name="cadastrar"),
    re_path("test-token", test_token, name="test-token"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
