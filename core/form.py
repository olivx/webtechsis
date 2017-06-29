from django import forms

from .models import Contact, ProdutoPytech


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('nome', 'categoria', 'assunto', 'menssagem')


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = ProdutoPytech
        fields = ('desc', 'sn')
