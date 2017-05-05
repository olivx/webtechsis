from django.test import TestCase

from core.models import Contact


class TestModelContact(TestCase):

    def test_create_contact(self):
        '''Test if create  a fit object on database '''
        contatct =  Contact.objects.create(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        self.assertTrue(contatct)







































