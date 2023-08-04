from rest_framework.serializers import ModelSerializer

from livraria.models import Autor, Categoria, Editora, Livro


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
