import json

from django.core import serializers
from django.shortcuts import resolve_url as r
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from core.form import LisenceADDForm
from core.models import Clientes, PerennityLicense
from core.form import LisenceADDForm
# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def license_prennity(request):
    licenses =  PerennityLicense.objects.all()

    add_form = LisenceADDForm()
    context = {
        'add_form': add_form,
        'licenses': licenses
    }

    return render(request, 'license_perennity.html', context)


@login_required
def autocomplete_clientes(request):
    ''' auto complete para clientes, retorna um json com os clientes que conferem com o parametro passado '''
    term = request.GET.get('term')
    if term:
        clientes =  Clientes.objects.using('techcd').filter(name__contains=term)[:10]
        results = []
        for cliente in clientes:
            json_cliente = {}
            json_cliente['id'] = cliente.id
            json_cliente['label'] =  cliente.name
            json_cliente['value'] =  cliente.name
            results.append(json_cliente)

        data = json.dumps(results)
        return  HttpResponse(data, 'application/json')

    return render(request, 'license_perennity.html')


@login_required
def save_lisence_perennity(request):

    if request.method == 'POST':
        form = LisenceADDForm(request.POST)
        if form.is_valid():
            license = PerennityLicense.objects.create(**form.cleaned_data,tecnico=request.user)
            print(license)
        print(form.cleaned_data)

    return HttpResponseRedirect(r('licenses'))

def license_detail(request, id):
    license = PerennityLicense.objects.filter(pk=id)
    data =  serializers.serialize('json', license)
    return HttpResponse(data, 'application/json')


