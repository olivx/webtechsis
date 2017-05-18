from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template.loader import render_to_string

from suporte.forms import LicenseForm
from suporte.models import PerennityLicense


# def não sendo mais usanda mais vou deixar ai por enquato...  para alguma consulta sei la
def serialze(license):
    keys = ('id', 'cliente', 'mac_address', 'serial', 'valid', 'installed', 'key', 'tecnico_name')
    return {key: getattr(license, key) for key in keys}


@login_required
def license_list(request):
    '''List the objects in table table_license '''

    search = request.GET.get('lisence-search')

    if search == None or search == '':
        licenses_list = PerennityLicense.objects.all().order_by('-id')

    else:
        licenses_list = PerennityLicense.objects.filter(Q(cliente__contains=search) |
                                                        Q(mac_address__contains=search) |
                                                        Q(serial__contains=search)).order_by('-id')

    paginator = Paginator(licenses_list, 5)
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
def license_form_service(request, form, template, sucess_message):
    data = {}

    if request.method == 'POST':
        if form.is_valid():
            license = form.save(commit=False)
            license.tecnico = request.user
            license.save()

            licenses_list = PerennityLicense.objects.all()
            paginator = Paginator(licenses_list, 5)
            try:
                page = int(request.GET.get('page','1'))
            except:
                page = 1
            try:
                licenses = paginator.page(page)
            except(EmptyPage, InvalidPage):
                licenses = paginator.page(paginator.num_pages)

            data['table_license'] = render_to_string('snippet/license_table.html',
                                                     {'licenses': licenses}, request=request)
            data['is_form_valid'] = True
            data['js_title_message'] = sucess_message
            data['js_cliente'] = license.cliente
            data['js_serial'] = license.serial
        else:
            data['is_form_valid'] = False
            data['js-message'] = 'um erro ocorreu com este formulario'

    data['form_html'] = render_to_string(template, {'form': form}, request=request)
    return JsonResponse(data)

def licese_stop_send_warning(request):
    data = {}

    if request.method == 'POST':
        license = PerennityLicense.objects.filter(Q(cliente=request.POST.get('cliente')) &
                                                  Q(serial=request.POST.get('serial')) &
                                                  Q(mac_address=request.POST.get('mac_address'))
                                                  ).first()
        license.nao_enviar_aviso = True
        license.data_ultimo_aviso = datetime.now()
        license.save()

        data['js_title_message'] = 'Emails de Aviso ão serão mais enviado! '
        data['js_cliente'] = license.cliente
        data['js_serial'] = license.serial

    return JsonResponse(data)

def license_save(request):
    if request.method == 'POST':
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

