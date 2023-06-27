from rest_framework.serializers import ModelSerializer

from livraria.models import Categoria, Editora, Autor, Livro
        
class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"