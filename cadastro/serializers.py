from rest_framework.serializers import ModelSerializer
from cadastro.models import Aluno, Professor


class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"


class AlunoSerializerBasic(ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["id", "nome"]


class ProfessorSerializer(ModelSerializer):
    class Meta(object):
        model = Professor
        fields = "__all__"


class ProfessorSerializerBasic(ModelSerializer):
    class Meta:
        model = Professor
        fields = ["id", "nome", "area_de_atuação"]  # teste com utf-8
