from django import forms

from faturamento.models import BoletoTech, BoletoMidia, BoletoData


class BoletoTechForm(forms.ModelForm):
    empresa = forms.CharField(label='empresa',widget=forms.HiddenInput())
    class Meta:
        model = BoletoTech
        fields = ('nnum_bol', 'numdoc_bol', 'sac_bol', 'val_bol',
                  'data_bol', 'venc_bol', 'val_bol', 'empresa')


class BoletoMidiaForm(forms.ModelForm):
    empresa = forms.CharField(label='empresa', widget=forms.HiddenInput())
    class Meta:
        model = BoletoMidia
        fields = ('nnum_bol', 'numdoc_bol', 'sac_bol', 'val_bol',
                  'data_bol', 'venc_bol', 'val_bol')


class BoletoDataForm(forms.ModelForm):
    empresa = forms.CharField(label='empresa', widget=forms.HiddenInput())
    class Meta:
        model = BoletoData
        fields = ('nnum_bol', 'numdoc_bol', 'sac_bol', 'val_bol',
                  'data_bol', 'venc_bol', 'val_bol')
