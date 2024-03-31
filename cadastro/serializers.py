from rest_framework.serializers import ModelSerializer
from cadastro.models import Alunos


class AlunosSerializers(ModelSerializer):
    class Meta:
        model = Alunos
        fields = (
            "id",
            "nome",
            "foto",
            "sexo",
            "data_nascimento",
            "telefone",
            "cpf",
        )
