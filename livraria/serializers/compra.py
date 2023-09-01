from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from livraria.models import Compra, ItensCompra
        
class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    
    def get_total(self, obj):
        return obj.livro.preco * obj.quantidade

    class Meta:
        model = ItensCompra
        fields = ["livro", "quantidade"]
        depth = 1
        

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)

    class Meta:
        model = Compra
        fields = "__all__"
