import json

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.template.loader import render_to_string

from core.form import ContactForm
from core.models import Clientes
# Create your views here.

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

@login_required
def autocomplete_clientes(request):
    ''' auto complete para clientes, retorna um json com os clientes que conferem com o parametro passado '''
    term = request.GET.get('term')
    if term:
        clientes = Clientes.objects.using('techcd').filter(name__contains=term)[:10]
        results = []
        for cliente in clientes:
            json_cliente = {}
            json_cliente['id'] = cliente.id
            json_cliente['label'] = cliente.name
            json_cliente['value'] = cliente.name
            results.append(json_cliente)

        data = json.dumps(results)
        return HttpResponse(data, 'application/json')

    return render(request, 'license_perennity.html')


