from django import forms
from suporte.models import PerennityLicense
from django.contrib.auth.models import User



class LicenseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LicenseForm, self).__init__(*args, **kwargs)
        self.fields['tecnico'].queryset = User.objects.filter(groups__name='SUPORTE')

    class Meta:
        model = PerennityLicense
        fields = ('cliente','active' ,'mac_address','tecnico',
                 'tipo_license', 'serial', 'valid', 'installed', 'key',)
