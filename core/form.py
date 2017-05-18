from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nome', 'categoria', 'assunto', 'menssagem')
