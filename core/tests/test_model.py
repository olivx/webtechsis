from django.test.runner import DiscoverRunner
from  model_mommy import mommy
from django.test import TestCase

from core.models import Contact, Clientes


class TestModelContact(TestCase):
    def test_create_contact(self):
        '''Test if create  a fit object on database '''
        contatct = Contact.objects.create(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        self.assertTrue(contatct)


class TestModelCliente(TestCase):


    def test_getModel(self):
        '''Test if can get  cliente '''
        self.cliente = Clientes.objects.using('techcd').filter(name__contains='thiago').first()
