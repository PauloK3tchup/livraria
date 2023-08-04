from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Autor, Categoria, Editora, Livro
from livraria.serializers import (
    AutorSerializer,
    CategoriaSerializer,
    EditoraSerializer,
    LivroDetailSerializer,
    LivroListSerializer,
    LivroSerializer,
)


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
