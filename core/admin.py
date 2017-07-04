from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from core.models import Contact, Produtos, Categorias, ProdutoPytech

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'assunto', 'categoria', 'data_created')
    list_filter = ('categoria', 'user')


class CategoriaFilter(SimpleListFilter):
    title = 'Categoria'
    parameter_name = 'categoria'

    def lookups(self, request, model_admin):

        list_tuple = []
        for cat in Categorias.objects.using('techcd').filter(cod_cat__in=Produtos.list_cod_cat):
            list_tuple.append((cat.cod_cat, cat.desc_cat))

        return list_tuple

    def queryset(self, request, queryset):

        if self.value():
            return queryset.filter(categoria__cod_cat=self.value())
        else:
            return queryset

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    # pegai na ducmentação do django
    # https://docs.djangoproject.com/pt-br/1.10/topics/db/multi-db/

    using = 'techcd'

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super(ProdutosAdmin, self).get_queryset(request).using(self.using). \
            filter(categoria__cod_cat__in=Produtos.list_cod_cat)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super(ProdutosAdmin, self).\
            formfield_for_foreignkey(db_field, request, using='techcd', **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super(ProdutosAdmin, self)\
            .formfield_for_manytomany(db_field, request, using='techcd', **kwargs)

    list_per_page = 10
    list_filter = (CategoriaFilter,)
    list_select_related = ('categoria',)
    list_display = ('id', '__str__', 'categoria', 'saldo_prod', 'teorico_prod')
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