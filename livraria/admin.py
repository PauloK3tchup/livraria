from django.contrib import admin

from .models import Autor, Categoria, Editora, Livro, Compra, ItensCompra

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)

class ItensCompraInline(admin.TabularInline):
    model = ItensCompra
    
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = [ItensCompraInline]