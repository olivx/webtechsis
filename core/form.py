from django import forms

from .models import PerennityLicense, Contact


class LicenseForm(forms.ModelForm):
    class Meta:
        model = PerennityLicense
        fields = ('cliente', 'mac_address', 'serial', 'valid', 'installed', 'key',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nome', 'categoria', 'assunto', 'menssagem')
