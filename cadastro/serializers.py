from rest_framework.serializers import ModelSerializer
from cadastro.models import Alunos, Professor


class AlunosSerializers(ModelSerializer):
    class Meta:
        model = Alunos
        fields = "__all__"


class ProfessoresSerializers(ModelSerializer):
    class Meta(object):
        model = Professor
        fields = "__all__"
