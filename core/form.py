from django import forms

class LisenceADDForm(forms.Form):

    cliente =  forms.CharField(label='Cliente ', widget=forms.TextInput(
        attrs={'placeholder':'Nome do cliente que a lisença foi instalada' , 'class' : 'form-control'}))

    mac_address = forms.CharField(label="Mac Address ", widget=forms.TextInput(
        attrs={'placeholder':'Mac address da placa de rede', 'class':'form-control'}
    ))

    serial =       forms.CharField(label='SN Perennity', widget=forms.TextInput(
        attrs={'placeholder':'Serial de instalação do Perennity', 'class':'form-control'}
    ))

    installed =  forms.DateField(label='Instalado em', widget=forms.TextInput(
        attrs={'class':'form-control' , 'placeholder':'DD/MM/AAAA'}))

    valid =     forms.DateField(label='Valido até', widget=forms.TextInput(
        attrs={'class':'form-control' , 'placeholder':'DD/MM/AAAA'}))

    key =  forms.CharField(label='Licença de instalação' , widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows':'4'}
    ))
