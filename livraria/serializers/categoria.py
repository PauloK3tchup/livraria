from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Autor, Livro

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"