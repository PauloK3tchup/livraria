from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Autor, Livro
        
class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"