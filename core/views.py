import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from core.form import LicenseForm, ContactForm
from core.models import Clientes, PerennityLicense


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
            # todo envio do form e salvar ele no banco
            # todo controle das resposta para ele
            pass


    else:
        pass

    print(form)
    return render(request, template, {'form': form})



@login_required
def license_list(request):
    '''List the objects in table table_license '''
    licenses_list = PerennityLicense.objects.all()
    paginator = Paginator(licenses_list, 3)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        licenses = paginator.page(page)

    except(EmptyPage, InvalidPage):
        licenses = paginator.page(paginator.num_pages)

    add_form = LicenseForm()
    context = {
        'add_form': add_form,
        'licenses': licenses,
    }
    return render(request, 'license_perennity.html', context)



@login_required
def autocomplete_clientes(request):
    ''' auto complete para clientes, retorna um json com os clientes que conferem com o parametro passado '''
    term = request.GET.get('term')
    if term:
        clientes = Clientes.objects.using('techcd').filter(name__contains=term)[:10]
        print(clientes)
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
def license_form_service(request, form, template, sucess_message):
    data = {}

    print('GET:', request.GET)
    print('GET:', request.POST)

    if request.method == 'POST':
        if form.is_valid():
            license = form.save(commit=False)
            license.tecnico = request.user
            license.save()

            licenses_list = PerennityLicense.objects.all()
            # paginator = Paginator(licenses_list, 3)
            # try:
            #     page = int(request.GET.get('page','1'))
            # except:
            #     page = 1
            # try:
            #     licenses = paginator.page(page)
            # except(EmptyPage, InvalidPage):
            #     licenses = paginator.page(paginator.num_pages)

            data['table_license'] = render_to_string('snippet/license_table.html',
                                                     {'licenses': licenses_list}, request=request)
            data['is_form_valid'] = True
            data['js_title_message'] = sucess_message
            data['js_cliente'] = license.cliente
            data['js_serial'] = license.serial
        else:
            data['is_form_valid'] = False
            data['js-message'] = 'um erro ocorreu com este formulario'

    data['form_html'] = render_to_string(template, {'form': form})
    return JsonResponse(data)


def license_save(request):
    if request.method == 'POST':
        print(request.POST)
        form = LicenseForm(request.POST)
    else:
        form = LicenseForm()
    return license_form_service(request, form, 'snippet/license_form_create.html', 'Licença criada com sucesso !')


def license_update(request, pk):
    license = get_object_or_404(PerennityLicense, pk=pk)

    if request.method == 'POST':
        form = LicenseForm(request.POST, instance=license)
    else:

        form = LicenseForm(instance=license)
    return license_form_service(request, form, 'snippet/license_form_update.html', 'Licença alterada  com sucesso !')


def license_delete(request, pk):
    data = {}
    license = get_object_or_404(PerennityLicense, pk=pk)

    if request.method == 'POST':
        license.delete()
        licenses = PerennityLicense.objects.all()
        data['table_license'] = render_to_string('snippet/license_table.html', {'licenses': licenses}, request=request)

        data['is_form_valid'] = True
        data['js_title_message'] = 'Licença Deletada com sucesso!'
        data['js_cliente'] = license.cliente
        data['js_serial'] = license.serial

    else:
        data['is_form_valid'] = False
        data['form_html'] = render_to_string('snippet/license_form_delete.html',
                                             {'form': LicenseForm(instance=license)}, request=request)

    return JsonResponse(data)


# def não sendo mais usanda mais vou deixar ai por enquato...  para alguma consulta sei la
def serialze(license):
    keys = ('id', 'cliente', 'mac_address', 'serial', 'valid', 'installed', 'key', 'tecnico_name')
    return {key: getattr(license, key) for key in keys}
