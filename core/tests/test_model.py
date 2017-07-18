from django.db.models import Q
from  model_mommy import mommy
from django.test import TestCase
from django.utils import timezone

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
        self.user = TechUser.objects.create \
            (username='thiagooliveira', password='logan')
        self.cliente = Clientes.objects.create \
            (cod_cli=1, name='thiago oliveira')

        self.group = GrupoUsuarios.objects.create \
            (cod_grupo=1, desc_grupo='sistema')

        self.categoria = Categorias.objects.create \
            (cod_cat=1, desc_cat='publicadores', )

        self.produto = Produtos.objects.create \
            (cod_prod=1, name='epson pp 100', categoria=self.categoria)

    def tearDown(self):
        self.cliente.delete()
        self.group.delete()
        self.categoria.delete()
        self.user.delete()
        self.produto.delete()

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
        """Test str tech user"""
        self.assertEqual('thiagooliveira', self.user.__str__())


class TestContrato(TestCase):

    def _setUp(self):
        self.cliente = Clientes.objects.create\
            (cod_cli=1, name='thiafo de oliveira')
        self.tipo = TipoContrato.objects.create\
            (cod_tip_cont=1, nome_tip_cont='nome tipo contrato', desc_tipo_cont='desc tipo contrato')
        self.contrato = Contrato.objects.create\
            (cod_contrato=1, cod_tip_cont=self.tipo, num_contrato='2016-003-00', empresa='t', data_criacao=timezone.now())
        self.unidae_negocio =  UnidadeNegocio.objects.create\
            (cod_unid_neg = 1, nivel = '1.1', nome_unid_neg='nome unidade neg', desc_unid_nego='desc unidade neg')

        self.contrato_cliente = ContratoCliente.objects.create\
            (cod_contrato=self.contrato, cod_cli =self.cliente, unidade_negocio=self.unidae_negocio)


        self.contratos = ContratoCliente.objects.select_related().all()

    def tearDown(self):
        self.cliente.delete()
        self.tipo.delete()
        self.contrato.delete()
        self.unidae_negocio.delete()
        self.contrato_cliente.delete()

    def test_is_instance_contato_cliente(self):
        """is instace contrato client """
        self.assertIsInstance(self.contrato_cliente, ContratoCliente)

    def test_has_instace_cliente(self):
        """is instace client """
        self.assertIsInstance(self.contrato_cliente.cod_cli, Clientes)

    def test_has_instace_contrato(self):
        """is instace contrato """
        self.assertIsInstance(self.contrato_cliente.cod_contrato, Contrato)

    def test_has_instace_unidade_negocio(self):
        """is instace unidade de negocio """
        self.assertIsInstance(self.contrato_cliente.unidade_negocio, UnidadeNegocio)

    def test_has_instace_tipo_contrato(self):
        """is instace unidade de tipo contrato """
        self.assertIsInstance(self.contrato_cliente.cod_contrato.cod_tip_cont, TipoContrato)
#

