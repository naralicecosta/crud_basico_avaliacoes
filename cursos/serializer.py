from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True} #O WriteOnly significa que o e-mail será exigido apenas quando for feito o cadastro, ou seja, na hora de consultar o e-mail ficará oculto.
        }
        model = Avaliacaofields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        )
