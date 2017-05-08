from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.db.models import Q

from faturamento.forms import BoletoTechForm, BoletoDataForm, BoletoMidiaForm
from faturamento.models import BoletoData, BoletoMidia, BoletoTech, ItemNfeSaidaPagtoDataSRV, ItemNfeSaidaPagtoData, \
    ItemNfeSaidaPagtoMidiaSRV, ItemNfeSaidaPagtoMidia
from faturamento.models import ItemNfeSaidaPagtoTech, ItemNfeSaidaPagtoTechSRV


def get_boletos(request, empresa):
    if empresa == 'data':
        if request.GET.get('search') is not '':
            boleto_list = BoletoData.objects.using('techcd') \
                .filter(Q(numdoc_bol=request.GET.get('search'))).order_by('-nnum_bol')
        else:
            boleto_list = BoletoData.objects.using('techcd').order_by('-nnum_bol')[:10]

    elif empresa == 'midia':
        if request.GET.get('search') is not '':
            boleto_list = BoletoMidia.objects.using('techcd') \
                .filter(Q(numdoc_bol=request.GET.get('search'))).order_by('-nnum_bol')
        else:
            boleto_list = BoletoMidia.objects.using('techcd').order_by('-nnum_bol')[:10]

    else:
        if request.GET.get('search') is not '':
            boleto_list = BoletoTech.objects.using('techcd') \
                .filter(Q(numdoc_bol=request.GET.get('search'))).order_by('-nnum_bol')
        else:
            boleto_list = BoletoTech.objects.using('techcd').order_by('-nnum_bol')[:10]

    return boleto_list


def boleto_list(request):
    template = 'faturamento/boletos_list.html'
    empresa = request.GET.get('radio-empresa')

    boleto_list = get_boletos(request, empresa)

    context = {'boletos': boleto_list, 'empresa': empresa}
    return render(request, template, context)


def boleto_tech_detail(request, nnum_bol):
    boleto = get_object_or_404(BoletoTech.objects.using('techcd'), nnum_bol=nnum_bol)
    form = BoletoTechForm(instance=boleto)
    return render(request, 'faturamento/boleto.html', {'form': form, 'empresa': 'TechCD'})


def boleto_data_detail(request, nnum_bol):
    boleto = get_object_or_404(BoletoData.objects.using('techcd'), nnum_bol=nnum_bol)
    form = BoletoDataForm(instance=boleto)
    return render(request, 'faturamento/boleto.html', {'form': form, 'empresa': 'Data Store'})


def boleto_midia_detail(request, nnum_bol):
    boleto = get_object_or_404(BoletoMidia.objects.using('techcd'), nnum_bol=nnum_bol)
    form = BoletoMidiaForm(instance=boleto)
    return render(request, 'faturamento/boleto.html', {'form': form, 'empresa': 'Midia Center'})


def boleto_update(request, nnum_bol):
    if request.POST:
        empresa = request.POST.get('empresa')
        # verifica de qual empresa é para montar o form
        if empresa == 'TechCD':
            boleto = get_object_or_404(BoletoTech.objects.using('techcd'), nnum_bol=nnum_bol)
            form = BoletoTechForm(request.POST, instance=boleto)
            if boleto.ind_tip_nfe_srv:
                item_pag = get_object_or_404(ItemNfeSaidaPagtoTechSRV.objects.using('techcd'),
                                             cod_nf_saida=boleto.numdoc_bol, datavencnf_saida_pagto=boleto.venc_bol)
            else:

                item_pag = get_object_or_404(ItemNfeSaidaPagtoTech.objects.using('techcd'),
                                             cod_nf_saida=boleto.numdoc_bol, datavencnf_saida_pagto=boleto.venc_bol)


        elif empresa == 'Data Store':
            boleto = get_object_or_404(BoletoData.objects.using('techcd'), nnum_bol=nnum_bol)
            form = BoletoDataForm(request.POST, instance=boleto)
            if boleto.ind_tip_nfe_srv:
                item_pag = get_object_or_404(ItemNfeSaidaPagtoDataSRV.objects.using('techcd'),
                                             cod_nf_saida=boleto.numdoc_bol, datavencnf_saida_pagto=boleto.venc_bol)
            else:

                item_pag = get_object_or_404(ItemNfeSaidaPagtoData.objects.using('techcd'),
                                             cod_nf_saida=boleto.numdoc_bol, datavencnf_saida_pagto=boleto.venc_bol)
        else:
            boleto = get_object_or_404(BoletoMidia.objects.using('techcd'), nnum_bol=nnum_bol)
            form = BoletoDataForm(request.POST, instance=boleto)
            if boleto.ind_tip_nfe_srv:
                item_pag = get_object_or_404(ItemNfeSaidaPagtoMidiaSRV.objects.using('techcd'),
                                             cod_nf_saida=boleto.numdoc_bol, datavencnf_saida_pagto=boleto.venc_bol)
            else:

                item_pag = get_object_or_404(ItemNfeSaidaPagtoMidia.objects.using('techcd'),
                                             cod_nf_saida=boleto.numdoc_bol, datavencnf_saida_pagto=boleto.venc_bol)

                # salva o boleto
        if form.is_valid():
            bol = form.save()

            _instance = type(item_pag)
            _instance.objects.using('techcd'). \
                filter(Q(cod_nf_saida=item_pag.cod_nf_saida) &
                       Q(datavencnf_saida_pagto=item_pag.datavencnf_saida_pagto)). \
                update(datavencnf_saida_pagto=bol.venc_bol, valnf_saida_pagto=bol.val_bol)
            messages.success(request, 'NFe {0}  da  {1}  Alterada  com Sucesso!'.format(boleto.numdoc_bol, empresa))
        else:
            form = BoletoTechForm(request.POST)

    return render(request, 'faturamento/boleto.html', {'form': form})
