from django.core.management.base import BaseCommand

from core.models import Clientes


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--all', '-a',
            action='store_true',
            help='print all contract'
        )

    def handle(self, *args, **options):
        clientes = Clientes.objects.filter(cod_cli__lte=100)
        for cliente in clientes:
            print(cliente.cod_cli, cliente)