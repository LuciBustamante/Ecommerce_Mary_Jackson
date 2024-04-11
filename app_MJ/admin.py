from django.contrib import admin
from django.utils.html import format_html
from .models import *

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto', 'categoria', 'preco', 'quantidade', 'mostrar_imagem')
    ordering = ('nome_produto', 'categoria', 'preco', 'quantidade')

    def mostrar_imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" alt="{}" style="max-width:100px; max-height:100px;" />',
                               obj.imagem.url, obj.nome_produto)
        else:
            return "Nenhuma imagem disponível"

    mostrar_imagem.allow_tags = True
    mostrar_imagem.short_description = 'Imagem'


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cidade', 'estado', 'telefone', 'email')
    ordering = ('nome_completo',)

class CarrinhoProdutoInline(admin.TabularInline):
    model = CarrinhoProduto
    extra = 1  

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'data_pedido')
    ordering = ('cliente', 'data_pedido')
    inlines = (CarrinhoProdutoInline,)

class CarrinhoProdutoAdmin(admin.ModelAdmin):
    list_display = ('carrinho', 'cliente_e_produtos', 'quantidade', 'preco', 'data_pedido')
    ordering = ('carrinho', 'produto', 'quantidade', 'preco', 'data_pedido')  

    def cliente_e_produtos(self, obj):
        produtos = ", ".join([carrinho_produto.produto.nome_produto for carrinho_produto in CarrinhoProduto.objects.filter(carrinho=obj.carrinho)])
        return produtos

    cliente_e_produtos.short_description = 'Produtos'


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(CarrinhoProduto, CarrinhoProdutoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
