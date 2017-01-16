import json
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from core.form import LisenceADDForm
from core.models import Clientes, PerennityLicense


# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


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


@login_required
def license_prennity(request):
    licenses = PerennityLicense.objects.all()
    add_form = LisenceADDForm()
    context = {
        'add_form': add_form,
        'licenses': licenses,
    }
    return render(request, 'license_perennity.html', context)


@login_required
def save_lisence_perennity(request):
    data = {}
    if request.method == 'POST':

        form = LisenceADDForm(request.POST)
        serial = None
        license = None
        if form.is_valid():
            serial = form.cleaned_data.get('serial')
            try:
                PerennityLicense.objects.get(serial=serial)
                PerennityLicense.objects.filter(serial=serial).update(**form.cleaned_data, tecnico=request.user)
                license = PerennityLicense.objects.get(serial=serial)
                data['is_form_valid'] = True
                data['method'] = 'update'
                data['title'] = 'update realizado com sucesso!'
            except PerennityLicense.DoesNotExist:
                license = PerennityLicense.objects.create(**form.cleaned_data, tecnico=request.user)
                data['is_form_valid'] = True
                data['method'] = 'create'
                data['title'] = 'cliente inserido com sucesso!'

        else:
            data['is_form_valid'] = False

        data['licenses'] = {'license': serialze(license)}
        data['cliente'] = 'CLIENTE: %s ' % (form.cleaned_data.get('cliente'))
        data['serial'] = 'SERIAL: %s' % (form.cleaned_data.get('serial'))
    return JsonResponse(data)


@property
def tecnico(self):
    names = (self.first_name, self.last_name)
    return ' '.join(names) or None


def serialze(license):
    keys = ('id', 'cliente', 'mac_address', 'serial', 'valid', 'installed', 'key', 'tecnico_name')
    return {key: getattr(license, key) for key in keys}


@csrf_exempt
def license_detail(request):
    id = request.GET.get('license_id')
    license = PerennityLicense.objects.filter(pk=id)[0]
    data = serialze(license=license)
    return JsonResponse(data)


def deactivate_license_perennity(request):
    if request.POST:
        print(request.POST)
        id = request.POST.get('id_license')
        PerennityLicense.objects.filter(pk=id).update(active=False)

    return HttpResponseRedirect(r('licenses'))
