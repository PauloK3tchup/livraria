from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from livraria.models import Compra, ItensCompra
        
class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    
    def get_total(self, instance):
        return instance.livro.preco * instance.quantidade

    class Meta:
        model = ItensCompra
        fields = ["livro", "quantidade","total"]
        depth = 1
        

class CompraSerializer(ModelSerializer):
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("id", "usuario", "status", "total", "itens")

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item_data in itens_data:
            ItensCompra.objects.create(compra=compra, **item_data)
        compra.save()
        return compra
    
class CriarEditarItemCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("livro", "quantidade")
    
class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItemCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = ("usuario", "itens")
        