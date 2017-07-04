from django.db.models import Q
from  model_mommy import mommy
from django.test import TestCase

from core.models import *


class TestModelContact(TestCase):
    def test_create_contact(self):
        """Test if create  a fit object on database """
        contatct = Contact.objects.create(nome='thiago oliveira', categoria=Contact.SUGESTAO,
                                          assunto='teste de formulario', menssagem='Messangem teste')
        self.assertTrue(contatct)


class TestModelProdutoPyTech(TestCase):
    def setUp(self):
        self.rimage_robo = mommy.make(ProdutoPytech, desc='rimage 7100n', sn='123456')
        self.rimage_printer = mommy.make(ProdutoPytech, desc='prisma plus')
        self.cliente = mommy.make(ClientePytech, name='Centro de diagnostico de curitiba',
                                  nick_name='SIDI')

    def test_client_have_to_products(self):
        """The client can be have more than one product"""
        self.cliente.produtos.create(desc=self.rimage_robo.desc, sn=self.rimage_robo.sn)
        self.cliente.produtos.create(desc=self.rimage_printer.desc, sn=self.rimage_printer.sn)
        count = ClientePytech.objects.filter(produtos__cliente__isnull=False).count()
        self.assertEqual(count, 2)




class TestModelCliente(TestCase):
    def setUp(self):
        self.user = TechUser.objects.using('techcd').create \
            (username='thiagooliveira', password='logan')
        self.cliente = Clientes.objects.using('techcd').create \
            (id=1, name='thiago oliveira')

        self.group = GrupoUsuarios.objects.using('techcd').create \
            (cod_grupo=1, desc_grupo='sistema')

        self.categoria = Categorias.objects.using('techcd').create \
            (cod_cat=1, desc_cat='publicadores', )

        self.produto = Produtos.objects.using('techcd').create \
            (id=1, name='epson pp 100', categoria=self.categoria)

    def tearDown(self):
        self.cliente.delete()
        self.group.delete()
        self.categoria.delete()
        self.user.delete()

    def test_str(self):
        """Test __str__ is capitalize"""
        self.assertEqual(self.cliente.__str__(), 'Thiago Oliveira')

    def test_group_str(self):
        """Group __str__ must be upper case"""
        self.assertEqual('SISTEMA', self.group.__str__())

    def test_categoria_str_(self):
        """Categoria __str__  must be uppercase"""
        self.assertEqual('PUBLICADORES', self.categoria.__str__())

    def test_produtos_str_(self):
        """Produto must be upper case"""
        self.assertEqual('EPSON PP 100', self.produto.__str__())

    def test_techuser_client_str_(self):
        '''Test str tech user'''
        self.assertEqual('thiagooliveira', self.user.__str__())
