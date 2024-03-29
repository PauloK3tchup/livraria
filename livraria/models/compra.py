from django.db import models

from usuario.models import Usuario
from .livro import Livro

class Compra(models.Model):
    class StatusCompra(models.IntegerChoices):
        CARRINHO = (1, 'Carrinho',)
        REALIZADO = (2, 'Realizado',)
        PAGO = (3, 'Pago',)
        ENTREGUE = (4, 'Entregue',)
        
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='compras')
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO)
    # data = models.DateTimeField(auto_now_add=True)
    @property
    def total(self):
        # total = 0
        # for item in self.itens.all():
        #     total += item.livro.preco * item.quantidade
        # return total
        return sum(item.livro.preco * item.quantidade for item in self.itens.all())
    
class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="+")
    quantidade = models.IntegerField(default=1)