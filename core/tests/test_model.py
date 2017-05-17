from django.test import TestCase

from core.models import Contact, Produtos
from model_mommy import mommy


class TestModelContact(TestCase):

    def test_create_contact(self):
        '''Test if create  a fit object on database '''
        contatct =  Contact.objects.create(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        self.assertTrue(contatct)

# class TestProdutos(TestCase):
#     multi_db = True
#
#     def test_produtos_has_categorias(self):
#         '''Test if produtos has categoria'''
#         produto =  mommy.make(Produtos)
#         print(produto)
#









































