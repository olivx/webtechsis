import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websistesis.settings')
django.setup()
from datetime import date
from core.models import PerennityLicense
from django.core.mail import send_mail
from django.template.loader import render_to_string



def check_license():
    '''
    faz uma varredura no baco de dados e verifica as licenças que estão ativas e para vencer 
    se elas se enquadrarem no padrao de lista  time_is_out = [5, 4, 3, 2, 1, 0, -1, -2, -3]
    com 5 antes  ou 3 já vencidas deve ser enviado um e-mail para suporte@techcd.com.br 
    avisado a situação 
    '''
    time_is_out = [5, 4, 3, 2, 1, 0, -1, -2, -3]

    now = date.today()
    licenses = PerennityLicense.objects.filter(active=True)
    for license in licenses:
        time = license.valid - now
        if time.days in time_is_out:
            message = render_to_string('snippet/license_warning.txt', {'license' : license})
            subject =  'Licença do cliente: {0} expira em {1}'.format(license.cliente, license.valid.strftime('%d/%m/%Y'))
            send_mail(subject, message, 'thiago@techcd.com.br', ['suporte@techcd.com.br'] )

if __name__ == '__main__':
    check_license()
