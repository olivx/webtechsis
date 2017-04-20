from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in


class TechUser(models.Model):
    # cod_niv = models.ForeignKey('Niveis', models.DO_NOTHING, db_column='COD_NIV')  # Field name made lowercase.
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
    categoria =  models.IntegerField(choices=TIPO_CATEGORIAS, default=SUGESTAO)
    assunto = models.CharField(max_length=100,)
    menssagem =  models.TextField()
    data_created =  models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User, default=0 , null=True, blank=True)
    class Meta:
        ordering = ['-data_created']
        verbose_name =  'Contato'
        verbose_name_plural  = 'Contatos'

    def __str__(self):
        return self.assunto




class PerennityLicense(models.Model):
    tecnico = models.ForeignKey(User, related_name='tecnicos')

    cliente = models.CharField('Cliente', max_length=250)
    mac_address = models.CharField('MacAddress', max_length=250)
    serial = models.CharField('SN', max_length=100, unique=True, null=True, blank=True)
    installed = models.DateField('Instalado', null=True, blank=True)
    valid = models.DateField('Valido', null=True, blank=True)
    key = models.TextField('Chave', null=True, blank=True)
    active = models.NullBooleanField(default=True)

    class Meta:
        ordering = ['-valid']

    def __str__(self):
        return '%s | %s' % (self.cliente, self.mac_address)

    @property
    def tecnico_name(self):
        names = (self.tecnico.first_name, self.tecnico.last_name)
        return ' '.join(names) or None


class Clientes(models.Model):
    id = models.BigIntegerField(db_column='COD_CLI', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.

    # cod_vend = models.IntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    # pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # contato_cli = models.CharField(db_column='CONTATO_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    # email_cli = models.CharField(db_column='EMAIL_CLI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # email2_cli = models.CharField(db_column='EMAIL2_CLI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # num_cli = models.CharField(db_column='NUM_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # end2_cli = models.CharField(db_column='END2_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # num2_cli = models.CharField(db_column='NUM2_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # bair2_cli = models.CharField(db_column='BAIR2_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # cid2_cli = models.CharField(db_column='CID2_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # est2_cli = models.CharField(db_column='EST2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # cep2_cli = models.CharField(db_column='CEP2_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    # cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    # rg_cli = models.CharField(db_column='RG_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    # ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    # ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # ddd2_cli = models.CharField(db_column='DDD2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # tel2_cli = models.CharField(db_column='TEL2_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # ramal2_cli = models.CharField(db_column='RAMAL2_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # dddfax_cli = models.CharField(db_column='DDDFAX_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    # fax_cli = models.CharField(db_column='FAX_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    # ramalfax_cli = models.CharField(db_column='RAMALFAX_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    # obs_cli = models.TextField(db_column='OBS_CLI', blank=True, null=True)  # Field name made lowercase.
    # cod_divulg = models.BigIntegerField(db_column='COD_DIVULG', blank=True, null=True)  # Field name made lowercase.
    # semacresc_cli = models.NullBooleanField(db_column='SEMACRESC_CLI')  # Field name made lowercase.
    # aprazosemnf_cli = models.NullBooleanField(db_column='APRAZOSEMNF_CLI')  # Field name made lowercase.
    # precosprom_cli = models.NullBooleanField(db_column='PRECOSPROM_CLI')  # Field name made lowercase.
    # email_info_cli = models.NullBooleanField(db_column='EMAIL_INFO_CLI')  # Field name made lowercase.
    # dataincl_cli = models.DateTimeField(db_column='DATAINCL_CLI', blank=True, null=True)  # Field name made lowercase.
    # nome2_cli = models.CharField(db_column='NOME2_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    # cpf2_cli = models.CharField(db_column='CPF2_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    # cnpj2_cli = models.CharField(db_column='CNPJ2_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    # rg2_cli = models.CharField(db_column='RG2_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    # ie2_cli = models.CharField(db_column='IE2_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    # pes2_cli = models.CharField(db_column='PES2_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    # cod_at = models.BigIntegerField(db_column='COD_AT', blank=True, null=True)  # Field name made lowercase.
    # cod_cre = models.BigIntegerField(db_column='COD_CRE', blank=True, null=True)  # Field name made lowercase.
    # valid_cre = models.DateTimeField(db_column='VALID_CRE', blank=True, null=True)  # Field name made lowercase.
    # dt_alt_cad = models.DateTimeField(db_column='DT_ALT_CAD', blank=True, null=True)  # Field name made lowercase.
    # avisou_exp_cred = models.NullBooleanField(db_column='AVISOU_EXP_CRED')  # Field name made lowercase.
    # cargo_conta_cli = models.CharField(db_column='CARGO_CONTA_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # departamento_conta_cli = models.CharField(db_column='DEPARTAMENTO_CONTA_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # user_alt_cad = models.CharField(db_column='USER_ALT_CAD', max_length=30, blank=True,  null=True)  # Field name made lowercase.
    # tel_fin_cli = models.CharField(db_column='TEL_FIN_CLI', max_length=10, blank=True ,null=True)  # Field name made lowercase.
    # ddd_fin_cli = models.CharField(db_column='DDD_FIN_CLI', max_length=2, blank=True,  null=True)  # Field name made lowercase.
    # suframa_cli = models.CharField(db_column='SUFRAMA_CLI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    # contato_fin_cli = models.CharField(db_column='CONTATO_FIN_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    # bv_cli = models.IntegerField(blank=True, null=True)
    # rimage_cli = models.NullBooleanField(db_column='RIMAGE_CLI')  # Field name made lowercase.
    # emailnfe_cli = models.CharField(db_column='EmailNFE_CLI', max_length=50, blank=True,   null=True)  # Field name made lowercase.
    # datahab_cli = models.DateTimeField(db_column='dataHab_Cli', blank=True, null=True)  # Field name made lowercase.
    # quemhab_cli = models.CharField(db_column='QuemHab_Cli', max_length=30, blank=True,  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TECHCD].[DBO].[CLIENTES'
        # ordering = ['-name']

    def __str__(self):
        return self.name



        # macarrao que tinha feito , não é mais necessario
        # def get_tech_user_signal(sender, user, request, **kwargs):
        #     # if not user.is_superuser:
        #     #     test_user = TechDjangoUser.objects.get(django_user=user)
        #     #     tech_user = TechUser.objects.using('techcd').get(username=test_user.tech_user)
        #     #     request.session['tech_user'] = tech_user
        #
        # user_logged_in.connect(get_tech_user_signal)

#
