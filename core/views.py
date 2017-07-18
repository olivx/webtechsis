import json

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Q
from core.form import ContactForm, ProdutoForm
from core.models import Clientes, Produtos, ProdutoPytech, ContratoCliente, Contrato, TipoContrato, UnidadeNegocio

# Create your views here.
from core.utils import pagination


@login_required
def home(request):
    '''Render my home page'''
    return render(request, 'index.html')


def contact(request):
    template = 'contato.html'
    form = ContactForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            contact = form.save(commit=False)
            if request.user.is_authenticated:
                contact.user = request.user
            contact.save()
            body = render_to_string('snippet/contato.txt', {'contato': contact})
            send_mail(contact.assunto, body,
                      'thiago@techcd.com.br', ['thiago@techcd.com.br'])

            return HttpResponseRedirect(resolve_url('obrigado_pelo_contato'))

    return render(request, template, {'form': form})


def autocomplete(object_list):
    """ Generic autocomplete """
    results = []
    for object in object_list:
        json_ = {}
        json_['id'] = object.cod_cli
        json_['label'] = object.name.upper()
        json_['value'] = object.name.upper()
        results.append(json_)

    data = json.dumps(results)
    return data


@login_required
def autocomplete_clientes(request):
    """ auto complete para clientes, retorna um json com os clientes que conferem com o parametro passado """
    term = request.GET.get('term')
    if term:
        object_list = Clientes.objects.using('techcd').filter(name__contains=term)[:10]
        data = autocomplete(object_list)
        return HttpResponse(data, 'application/json')
    return render(request, 'license_perennity.html')


@login_required
def autocomplete_produtos(request):
    """auto complete para produtos, retorna um json com os mesmo """
    term = request.GET.get('term')
    if term:
        object_list = Produtos.objects.using('techcd').filter(name__icontains=term)[:10]
        for object in object_list:
            print(object)
        data = autocomplete(object_list)
        return HttpResponse(data, 'application/json')
    return render(request, 'produtos.html')


@login_required
def produtos(request):
    _search = request.GET.get('search')
    print(_search)

    if _search is not None:
        product_list = ProdutoPytech.objects.filter(Q(sn=_search) | Q(desc__contains=_search) & Q(ativo=True))
    else:
        product_list = ProdutoPytech.objects.filter(ativo=True)
    produto_paginator = pagination(request, product_list, 7)
    context = {
        'produto': produto_paginator
    }
    return render(request, 'produtos.html', context)


@login_required
def produto_form_services(request, form, template_name, message):
    data = {}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            produtos = ProdutoPytech.objects.filter(ativo=True)
            produto_paginator = pagination(request, produtos)
            data['is_form_valid'] = True
            data['message'] = message
            data['html_table'] = render_to_string('produtos/produto_table.html',
                                                  {'produto': produto_paginator}, request=request)
        else:
            data['is_form_valid'] = False
            data['message'] = 'erros foram encontrados durante o processo, verifique tente novamente.'
            data['html_form'] = \
                render_to_string(template_name, context={'form': form}, request=request)

    else:
        data['html_form'] = render_to_string(template_name, context={'form': form}, request=request)

    return JsonResponse(data)


@login_required
def produto_save(request):
    form = ProdutoForm(request.POST or None)
    return produto_form_services(request, form, 'produtos/produto_modal_create.html',
                                 'Produto incluido com sucesso.')


@login_required
def produto_update(request, pk):
    product = get_object_or_404(ProdutoPytech, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=product)
    else:
        form = ProdutoForm(instance=product)

    return produto_form_services(request, form, 'produtos/produto_update_form.html',
                                 'Produto Alterado com sucesso! ')


@login_required
def produto_delete(request, pk):
    data = {}
    template_name = 'produtos/produto_delete_form.html'
    product = get_object_or_404(ProdutoPytech, pk=pk)
    if request.method == 'POST':
        product.ativo = False
        product.save()
        produtos = ProdutoPytech.objects.filter(ativo=True)
        produto_paginator = pagination(request, produtos)

        data['is_form_valid'] = True
        data['message'] = 'Produto: {} \ndesativado com Sucesso.' \
                          'esse produto pode ser acessado somente na area de administração. ' \
            .format(product.desc)

        data['html_table'] = render_to_string('produtos/produto_table.html',
                                              {'produto': produto_paginator}, request=request)
    else:
        form = ProdutoForm(instance=product)
        data['html_form'] = \
            render_to_string(template_name, context={'form': form}, request=request)

    return JsonResponse(data)


@login_required
def contrato_client_list(request):


    search = request.GET.get('search')
    if search is not None:
        contrato_cliente = ContratoCliente.objects.select_related().using('techcd').filter(
            Q(cod_contrato__num_contrato=search) |
            Q(cod_cli__name__contains=search)
        )
    else:
        contrato_cliente = ContratoCliente.objects.select_related().using('techcd').all()

    contrato_cliente_list = pagination(request, contrato_cliente, 10)
    context = {
        'contrato_cliente_list': contrato_cliente_list
    }
    return render(request, 'client_list.html', context)
