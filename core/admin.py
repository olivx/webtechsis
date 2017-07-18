from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from core.models import Contact, Produtos, Categorias, ProdutoPytech, Contrato


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'assunto', 'categoria', 'data_created')
    list_filter = ('categoria', 'user')


class CategoriaFilter(SimpleListFilter):
    title = 'Categoria'
    parameter_name = 'categoria'

    def lookups(self, request, model_admin):
        list_tuple = []
        for cat in Categorias.objects.filter(cod_cat__in=Produtos.list_cod_cat):
            list_tuple.append((cat.cod_cat, cat.desc_cat))

        return list_tuple
    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(categoria__cod_cat=self.value())
        else:
            return queryset

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = (CategoriaFilter,)
    list_select_related = ('categoria',)
    list_display = ('cod_prod', '__str__', 'categoria', 'saldo_prod', 'teorico_prod')
    search_fields = ('name', 'categoria__desc_cat',)

    @staticmethod
    def categoria(object):
        categorias = object.categoria
        return categorias


@admin.register(ProdutoPytech)
class PytechProdutos(admin.ModelAdmin):
    list_filter = ('ativo', )
    list_display = ('desc','sn', 'ativo')
    search_fields = ('desc', 'sn')
    list_per_page = 10

