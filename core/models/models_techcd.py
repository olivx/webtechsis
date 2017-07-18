from django.conf import settings
from core.manage import *


class TechUser(models.Model):
    cod_grupo = models.OneToOneField('GrupoUsuarios', db_column='COD_GRUPO', blank=True, null=True,
                                     related_name='groups')  # Field name made lowercase.
    username = models.CharField(db_column='NOME_USER', primary_key=True, max_length=30,
                                unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='SENHA_USER', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP_HOST', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='APELIDO_USER', max_length=20, blank=True,
                                null=True)  # Field name made lowercase.
    skype = models.CharField(db_column='APELIDO_SKYPE', max_length=40, blank=True,
                             null=True)  # Field name made lowercase.

    objects = TechUserManager()

    def __str__(self):
        return self.username

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'USUARIOS'


class GrupoUsuarios(models.Model):
    cod_grupo = models.BigIntegerField(primary_key=True)
    desc_grupo = models.CharField(max_length=20, blank=True, null=True)

    objects = GrupoUsuarioManager()

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'GRUPO_USUARIOS'

    def __str__(self):
        return self.desc_grupo.upper()


class Clientes(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.

    objects = ClienteManager()

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'CLIENTES'

    def __str__(self):
        name = [n.capitalize() for n in self.name.split()]
        return ' '.join(name)


class Categorias(models.Model):
    cod_cat = models.BigIntegerField(db_column='COD_CAT', primary_key=True)  # Field name made lowercase.
    desc_cat = models.CharField(db_column='DESC_CAT', max_length=40, blank=True,
                                null=True)  # Field name made lowercase.
    cod_supercat = models.BigIntegerField(db_column='COD_SUPERCAT', blank=True, null=True)  # Field name made lowercase.
    mostrar_cat = models.CharField(db_column='MOSTRAR_CAT', max_length=17, blank=True,
                                   null=True)  # Field name made lowercase.
    apelido_cat = models.CharField(db_column='APELIDO_CAT', max_length=50, blank=True,
                                   null=True)  # Field name made lowercase.

    objects = CategoriaProdutoTechManager()

    def __str__(self):
        return self.desc_cat.upper()

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'CATEGORIAS'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Produtos(models.Model):
    """  categorias
     categorias relacionada ao suporte 
     174 =  Gravadore 
     42 =  equipamentos 
     45 =  suprimetos epson 
     46 =  serviços 
     49 =  suprimetos rimagem 
     52 =  produtos rimage 
     62 = produtos epson 
     63 = vidar equipametos 
     64 = vidar peças 
     57 = licença
     69 =  monitores 
     71 =  prdutos stratasys 
    """
    list_cod_cat = [174, 42, 45, 46, 49, 52, 62, 63, 64, 68, 69, 71]

    cod_prod = models.BigIntegerField(db_column='COD_PROD', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='DESC_PROD', max_length=300, blank=True,
                            null=True)  # Field name made lowercase.
    min_prod = models.IntegerField(db_column='MIN_PROD', blank=True, null=True)  # Field name made lowercase.
    saldo_prod = models.BigIntegerField(db_column='SALDO_PROD', blank=True, null=True)  # Field name made lowercase.
    teorico_prod = models.BigIntegerField(db_column='TEORICO_PROD', blank=True, null=True)  # Field name made lowercase.
    custoref_prod = models.DecimalField(db_column='CUSTOREF_PROD', max_digits=19, decimal_places=4, blank=True,
                                        null=True)  # Field name made lowercase.
    custo_prod = models.DecimalField(db_column='CUSTO_PROD', max_digits=19, decimal_places=4, blank=True,
                                     null=True)  # Field name made lowercase.

    categoria = models.ForeignKey(Categorias, db_column='COD_CAT', blank=True, null=True,
                                  related_name='categorias')  # Field name made lowercase.

    objects = ProdutoTechManager()

    def __str__(self):
        return self.name.upper()

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'PRODUTOS'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


# contrato

class Contrato(models.Model):
    cod_contrato = models.BigAutoField(db_column='COD_CONTRATO', primary_key=True)  # Field name made lowercase.
    cod_tip_cont = models.ForeignKey('TipoContrato', db_column='COD_TIP_CONT',
                                     related_name='tipos')  # Field name made lowercase.
    num_contrato = models.CharField(db_column='NUM_CONTRATO', max_length=11)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=1)  # Field name made lowercase.
    data_criacao = models.DateTimeField(db_column='DATA_CRIACAO')  # Field name made lowercase.
    ind_ativo = models.NullBooleanField(db_column='IND_ATIVO')

    def __str__(self):
        return self.num_contrato

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'CONTRATO'


class TipoContrato(models.Model):
    cod_tip_cont = models.BigAutoField(db_column='COD_TIP_CONT', primary_key=True)  # Field name made lowercase.
    nome_tip_cont = models.CharField(db_column='NOME_TIP_CONT', max_length=30)  # Field name made lowercase.
    desc_tipo_cont = models.CharField(db_column='DESC_TIPO_CONT', max_length=200)  # Field name made lowercase.

    def __str__(self):
        return self.nome_tip_cont

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'TIPO_CONTRATO'


class ContratoCliente(models.Model):
    cod_contrato = models.ForeignKey(Contrato, db_column='COD_CONTRATO')  # Field name made lowercase.
    cod_cli = models.ForeignKey('Clientes', db_column='COD_CLI', related_name='clientes')  # Field name made lowercase.
    unidade_negocio = models.ForeignKey('UnidadeNegocio', db_column='COD_UNID_NEG',
                                        related_name='unidade_negicos')  # Field name made lowercase.

    def __str__(self):
        return str(self.cod_cli)

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'CONTRATO_CLIENTE'
        unique_together = ('cod_contrato', 'cod_cli')


class UnidadeNegocio(models.Model):
    cod_unid_neg = models.BigAutoField(db_column='COD_UNID_NEG', primary_key=True)  # Field name made lowercase.
    nivel = models.CharField(db_column='NIVEL', max_length=10)  # Field name made lowercase.
    nome_unid_neg = models.CharField(db_column='NOME_UNID_NEG', max_length=30)  # Field name made lowercase.
    desc_unid_nego = models.CharField(db_column='DESC_UNID_NEGO', max_length=200)  # Field name made lowercase.

    def __str__(self):
        return self.nome_unid_neg

    class Meta:
        managed = True if settings.RUNNING_UNIT_TESTS else False
        db_table = 'UNIDADE_NEGOCIO'
