from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from livraria.models import Categoria, Editora, Autor, Livro
from livraria.serializers import CategoriaSerializer, EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer, LivroListSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer