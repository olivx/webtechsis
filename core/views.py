import json
from datetime import date

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse , JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from django.views.decorators.csrf import csrf_exempt

from core.form import LisenceADDForm
from core.models import Clientes, PerennityLicense

# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def license_prennity(request):
    licenses =  PerennityLicense.objects.all()
    today = date.today()


    for license in licenses:
        print(license.serial , (license.valid.today() - today) )

    add_form = LisenceADDForm()
    context = {
        'add_form': add_form,
        'licenses': licenses,
        'today': today

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
            serial =  form.cleaned_data.get('serial')

            try:
                PerennityLicense.objects.get(serial=serial)
                PerennityLicense.objects.update(**form.cleaned_data, tecnico=request.user)
            except PerennityLicense.DoesNotExist:
                PerennityLicense.objects.create(**form.cleaned_data,tecnico=request.user)

    return HttpResponseRedirect(r('licenses'))

@csrf_exempt
def license_detail(request):
        id = request.GET.get('license_id')
        license = PerennityLicense.objects.filter(pk=id).values()
        data =  list(license)
        return JsonResponse(data, safe=False)



