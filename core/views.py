import json

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.template.loader import render_to_string

from core.form import ContactForm, ProdutoForm
from core.models import Clientes, Produtos, ProdutoPytech


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
        json_['id'] = object.id
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
    produtos = ProdutoPytech.objects.all()
    produto_paginator = pagination(request, produtos, 7)
    context = {
        'produto': produto_paginator
    }
    return render(request, 'produtos.html', context)


def produtos_save(request):
    data = {}
    template_name = 'produtos/produto_modal_create.html'
    form = ProdutoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            produtos = ProdutoPytech.objects.all()

            produto_paginator = pagination(request, produtos)
            data['is_form_valid'] = True
            data['html_table'] = render_to_string('produtos/produto_table.html',
                                                  {'produto': produto_paginator}, request=request)
        else:
            data['is_form_valid'] = False
            data['html_form'] = \
                render_to_string(template_name, context={'form': form}, request=request)

    else:
        data['html_form'] = render_to_string(template_name, context={'form': form}, request=request)

    return JsonResponse(data)
