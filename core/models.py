# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class TechUser(models.Model):
    # cod_niv = models.ForeignKey('Niveis', models.DO_NOTHING, db_column='COD_NIV')  # Field name made lowercase.
    cod_grupo = models.OneToOneField('GrupoUsuarios', db_column='COD_GRUPO', blank=True, null=True, related_name='groups')  # Field name made lowercase.
    username = models.CharField(db_column='NOME_USER', primary_key=True, max_length=30, unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='SENHA_USER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP_HOST', max_length=13, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='APELIDO_USER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    skype = models.CharField(db_column='APELIDO_SKYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.username

    class Meta:
        managed = False
        db_table = 'TECHCD].[DBO].[USUARIOS'

class GrupoUsuarios(models.Model):
    cod_grupo = models.BigIntegerField(primary_key=True)
    desc_grupo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TECHCD].[DBO].[GRUPO_USUARIOS'

    def __str__(self):
        return self.desc_grupo

class Contact(models.Model):
    SUGESTAO = 1
    SOLITACAO = 2
    RECALAMCAO = 3
    RECALAMCAO_ANONIMA = 4

    TIPO_CATEGORIAS = (
        (SUGESTAO, 'SUGESTÃO'),
        (SOLITACAO, 'SOLITAÇÃO'),
        (RECALAMCAO, 'RECLAMAÇÃO'),
        (RECALAMCAO_ANONIMA, 'RECLAMAÇÃO ANONIMA'),
    )

    nome = models.CharField(max_length=50, null=True, blank=True)
    categoria = models.IntegerField(choices=TIPO_CATEGORIAS, default=SUGESTAO)
    assunto = models.CharField(max_length=100, )
    menssagem = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=0, null=True, blank=True)

    class Meta:
        ordering = ['-data_created']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.assunto

class Clientes(models.Model):
    id = models.BigIntegerField(db_column='COD_CLI', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TECHCD].[DBO].[CLIENTES'
        # ordering = ['-name']

    def __str__(self):
        return self.name

class Categorias(models.Model):
    cod_cat = models.BigIntegerField(db_column='COD_CAT', primary_key=True)  # Field name made lowercase.
    desc_cat = models.CharField(db_column='DESC_CAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cod_supercat = models.BigIntegerField(db_column='COD_SUPERCAT', blank=True, null=True)  # Field name made lowercase.
    mostrar_cat = models.CharField(db_column='MOSTRAR_CAT', max_length=17, blank=True, null=True)  # Field name made lowercase.
    apelido_cat = models.CharField(db_column='APELIDO_CAT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.desc_cat

    class Meta:
        managed = False
        db_table = 'CATEGORIAS'
        verbose_name =  'Categoria'
        verbose_name_plural = 'Categorias'

class Produtos(models.Model):
    '''
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
    '''
    list_cod_cat = [174, 42, 45, 46, 49, 52, 62, 63, 64, 68, 69, 71]

    cod_prod = models.BigIntegerField(db_column='COD_PROD', primary_key=True)  # Field name made lowercase.
    desc_prod = models.CharField(db_column='DESC_PROD', max_length=300, blank=True, null=True)  # Field name made lowercase.
    min_prod = models.IntegerField(db_column='MIN_PROD', blank=True, null=True)  # Field name made lowercase.
    saldo_prod = models.BigIntegerField(db_column='SALDO_PROD', blank=True, null=True)  # Field name made lowercase.
    teorico_prod = models.BigIntegerField(db_column='TEORICO_PROD', blank=True, null=True)  # Field name made lowercase.
    custoref_prod = models.DecimalField(db_column='CUSTOREF_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    custo_prod = models.DecimalField(db_column='CUSTO_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.


    categoria = models.ForeignKey(Categorias, db_column='COD_CAT', blank=True, null=True, related_name='categorias')  # Field name made lowercase.


    def __str__(self):
        return self.desc_prod

    class Meta:
        managed = False
        db_table = 'PRODUTOS'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


