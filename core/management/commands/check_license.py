from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils.datetime_safe import date

from suporte.models import PerennityLicense


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--print', '-p',
                            action='store_true',
                            help='Ajuda da opção aqui.')

    def handle(self, *args, **options):
        time_is_out = [5, 4, 3, 2, 1, 0, -1, -2, -3]

        now = date.today()
        licenses = PerennityLicense.objects.filter(Q(active=True) & Q(nao_enviar_aviso=False))

        for license in licenses:
            time = license.valid - now
            if time.days in time_is_out:
                message = render_to_string('snippet/license_warning.txt', {'license': license})
                subject = 'Licença do cliente: {0} expira em {1}'.format(license.cliente,
                                                                         license.valid.strftime('%d/%m/%Y'))
                if options['print']:
                    self.stdout.write(subject)
                    self.stdout.write(message)
                    self.stdout.write('======================================================================')
                else:
                    send_mail(subject, message, 'thiago@techcd.com.br', ['suporte@techcd.com.br'])
