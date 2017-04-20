# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AssocFreteLocalidade(models.Model):
    cod_ent = models.ForeignKey('FreteRegiao', models.DO_NOTHING, db_column='COD_ENT')  # Field name made lowercase.
    sigla_regiao = models.ForeignKey('FreteRegiao', models.DO_NOTHING, db_column='SIGLA_REGIAO')  # Field name made lowercase.
    localidade = models.CharField(db_column='LOCALIDADE', max_length=30)  # Field name made lowercase.
    cep_ini = models.CharField(db_column='CEP_INI', max_length=8)  # Field name made lowercase.
    cep_fim = models.CharField(db_column='CEP_FIM', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASSOC_FRETE_LOCALIDADE'
        unique_together = (('cod_ent', 'sigla_regiao', 'cep_ini', 'cep_fim'),)


class AtividadesPf(models.Model):
    cod_ativ = models.IntegerField(db_column='COD_ATIV', primary_key=True)  # Field name made lowercase.
    desc_ativ = models.CharField(db_column='DESC_ATIV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cod_setor = models.ForeignKey('SetorAtuacao', models.DO_NOTHING, db_column='COD_SETOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATIVIDADES_PF'


class AtividadesPj(models.Model):
    cod_ativ = models.IntegerField(db_column='COD_ATIV', primary_key=True)  # Field name made lowercase.
    desc_ativ = models.CharField(db_column='DESC_ATIV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cod_setor = models.ForeignKey('SetorAtuacao', models.DO_NOTHING, db_column='COD_SETOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATIVIDADES_PJ'


class Atualizacoes(models.Model):
    cod_alt = models.BigIntegerField(db_column='COD_ALT', blank=True, null=True)  # Field name made lowercase.
    data_alt = models.DateTimeField(db_column='DATA_ALT', blank=True, null=True)  # Field name made lowercase.
    usuario_alt = models.CharField(db_column='USUARIO_ALT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    alteracao = models.TextField(db_column='ALTERACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATUALIZACOES'


class AtAgenda(models.Model):
    cod_age = models.BigAutoField(db_column='Cod_Age', primary_key=True)  # Field name made lowercase.
    cod_at = models.ForeignKey('Telemarketing', models.DO_NOTHING, db_column='Cod_AT')  # Field name made lowercase.
    cod_ativ = models.BigIntegerField(db_column='Cod_Ativ')  # Field name made lowercase.
    data_age = models.DateTimeField(db_column='Data_Age')  # Field name made lowercase.
    data2_age = models.DateTimeField(db_column='Data2_Age')  # Field name made lowercase.
    desc_age = models.CharField(db_column='Desc_Age', max_length=1000)  # Field name made lowercase.
    usu_age = models.CharField(db_column='Usu_Age', max_length=50)  # Field name made lowercase.
    vend_age = models.BigIntegerField(db_column='Vend_Age', blank=True, null=True)  # Field name made lowercase.
    feito_age = models.IntegerField(db_column='Feito_Age')  # Field name made lowercase.
    data3_age = models.DateTimeField(db_column='Data3_Age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AT_AGENDA'


class AtAtividade(models.Model):
    cod_ativ = models.BigIntegerField(db_column='Cod_Ativ', primary_key=True)  # Field name made lowercase.
    desc_ativ = models.CharField(db_column='Desc_Ativ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marcadata_ativ = models.NullBooleanField(db_column='MarcaData_Ativ')  # Field name made lowercase.
    transvenda_ativ = models.NullBooleanField(db_column='TransVenda_Ativ')  # Field name made lowercase.
    email = models.NullBooleanField(db_column='Email')  # Field name made lowercase.
    abrev_ativ = models.CharField(db_column='Abrev_ativ', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AT_ATIVIDADE'


class AtStatus(models.Model):
    cod_status = models.BigIntegerField(db_column='Cod_Status', primary_key=True)  # Field name made lowercase.
    desc_status = models.CharField(db_column='Desc_Status', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AT_STATUS'


class AutorizacaoDev(models.Model):
    cod_dev = models.ForeignKey('DevolucaoOs', models.DO_NOTHING, db_column='COD_DEV')  # Field name made lowercase.
    quem_autorizou = models.CharField(db_column='QUEM_AUTORIZOU', max_length=30)  # Field name made lowercase.
    data_hora_aut = models.DateTimeField(db_column='DATA_HORA_AUT')  # Field name made lowercase.
    obs_aut = models.TextField(db_column='OBS_AUT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUTORIZACAO_DEV'
        unique_together = (('cod_dev', 'quem_autorizou', 'data_hora_aut'),)


class AuxImp12042010(models.Model):
    cod_prod = models.BigIntegerField(blank=True, null=True)
    ativ = models.BigIntegerField(blank=True, null=True)
    saldo_prod = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AUX_IMP_12042010'


class AliquotaIcms(models.Model):
    uf = models.CharField(db_column='UF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aliq_interna = models.FloatField(db_column='Aliq_Interna', blank=True, null=True)  # Field name made lowercase.
    aliq_interestadual = models.FloatField(db_column='Aliq_Interestadual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aliquota_ICMS'


class Apagar2(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    saldo = models.BigIntegerField(db_column='SALDO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Apagar_2'


class ArquivoMortoPagtoPendentes(models.Model):
    cod_os = models.BigIntegerField(blank=True, null=True)
    parcnum_os = models.BigIntegerField(blank=True, null=True)
    cod_pagto = models.BigIntegerField(blank=True, null=True)
    cod_frmpagto = models.BigIntegerField(blank=True, null=True)
    val_pagto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    real_pagto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    datavenc_pagto = models.DateTimeField(blank=True, null=True)
    taxa_os = models.FloatField(blank=True, null=True)
    quit_os = models.NullBooleanField()
    quemquit_os = models.CharField(max_length=30, blank=True, null=True)
    dataquit_os = models.DateTimeField(blank=True, null=True)
    cod2_pagto = models.BigIntegerField(blank=True, null=True)
    cod2_frmpagto = models.BigIntegerField(blank=True, null=True)
    cod_banco = models.BigIntegerField(blank=True, null=True)
    chq_pagto = models.CharField(max_length=20, blank=True, null=True)
    capt_pagto = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'Arquivo_Morto_Pagto_Pendentes'


class BackupControleEntregas(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS')  # Field name made lowercase.
    dest_ctr = models.IntegerField(db_column='DEST_CTR', blank=True, null=True)  # Field name made lowercase.
    tipodest_ctr = models.CharField(db_column='TIPODEST_CTR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retirapagto_ctr = models.BooleanField(db_column='RETIRAPAGTO_CTR')  # Field name made lowercase.
    prazo_ctr = models.IntegerField(db_column='PRAZO_CTR', blank=True, null=True)  # Field name made lowercase.
    dtprevist_ctr = models.DateTimeField(db_column='DTPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist_ctr = models.DateTimeField(db_column='HRPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist2_ctr = models.DateTimeField(db_column='HRPREVIST2_CTR', blank=True, null=True)  # Field name made lowercase.
    val_ctr = models.DecimalField(db_column='VAL_CTR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_ctr = models.TextField(db_column='OBS_CTR', blank=True, null=True)  # Field name made lowercase.
    pto_ref = models.CharField(db_column='PTO_REF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paga_frete = models.NullBooleanField(db_column='PAGA_FRETE')  # Field name made lowercase.
    val_frete = models.DecimalField(db_column='VAL_FRETE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_ctr = models.NullBooleanField(db_column='CANC_CTR')  # Field name made lowercase.
    cod_mboy = models.BigIntegerField(db_column='COD_MBOY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BACKUP_CONTROLE_ENTREGAS'


class BackupControleEntregasAvulso(models.Model):
    cod_ctr = models.BigIntegerField(db_column='COD_CTR')  # Field name made lowercase.
    cod_func = models.IntegerField(db_column='COD_FUNC', blank=True, null=True)  # Field name made lowercase.
    dest_ctr = models.IntegerField(db_column='DEST_CTR', blank=True, null=True)  # Field name made lowercase.
    cod_conta = models.IntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    tipodest_ctr = models.CharField(db_column='TIPODEST_CTR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retirapagto_ctr = models.BooleanField(db_column='RETIRAPAGTO_CTR')  # Field name made lowercase.
    prazo_ctr = models.IntegerField(db_column='PRAZO_CTR', blank=True, null=True)  # Field name made lowercase.
    dtprevist_ctr = models.DateTimeField(db_column='DTPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist_ctr = models.DateTimeField(db_column='HRPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist2_ctr = models.DateTimeField(db_column='HRPREVIST2_CTR', blank=True, null=True)  # Field name made lowercase.
    val_ctr = models.DecimalField(db_column='VAL_CTR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_ctr = models.TextField(db_column='OBS_CTR', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.IntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    pto_ref = models.CharField(db_column='PTO_REF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paga_frete = models.NullBooleanField(db_column='PAGA_FRETE')  # Field name made lowercase.
    canc_ctr = models.SmallIntegerField(db_column='CANC_CTR', blank=True, null=True)  # Field name made lowercase.
    val_frete = models.DecimalField(db_column='VAL_FRETE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_mboy = models.SmallIntegerField(db_column='COD_MBOY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BACKUP_CONTROLE_ENTREGAS_AVULSO'


class Bancos(models.Model):
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', primary_key=True)  # Field name made lowercase.
    desc_banco = models.CharField(db_column='DESC_BANCO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    agen_banco = models.CharField(db_column='AGEN_BANCO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    conta_banco = models.CharField(db_column='CONTA_BANCO', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANCOS'


class BancoCliente(models.Model):
    cod_banco = models.BigIntegerField(db_column='Cod_Banco')  # Field name made lowercase.
    desc_banco = models.CharField(db_column='Desc_Banco', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cod_comp_banco = models.CharField(db_column='Cod_Comp_Banco', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANCO_CLIENTE'


class BoletosData(models.Model):
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol')  # Field name made lowercase.
    data_bol = models.DateTimeField(db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField(db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField(db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField(db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField(db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField(db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField(db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField(db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField(db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField(db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField(db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField(db_column='Env_Bol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_DATA'


class BoletosDataAux(models.Model):
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol', blank=True, null=True)  # Field name made lowercase.
    parcnf_saida_pagto = models.BigIntegerField(db_column='ParcNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_DATA_AUX'


class BoletosDataNfe(models.Model):
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol')  # Field name made lowercase.
    data_bol = models.DateTimeField(db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField(db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField(db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField(db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField(db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField(db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField(db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField(db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField(db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField(db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField(db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField(db_column='Env_Bol')  # Field name made lowercase.
    ind_tip_nfe_srv = models.NullBooleanField(db_column='IND_TIP_NFE_SRV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_DATA_NFE'


class BoletosDataNfeaux(models.Model):
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol', blank=True, null=True)  # Field name made lowercase.
    parcnf_saida_pagto = models.BigIntegerField(db_column='ParcNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    ind_tip_nfe_srv = models.NullBooleanField(db_column='IND_TIP_NFE_SRV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_DATA_NFEAUX'


class BoletosMidia(models.Model):
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol')  # Field name made lowercase.
    data_bol = models.DateTimeField(db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField(db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField(db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField(db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField(db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField(db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField(db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField(db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField(db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField(db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField(db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField(db_column='Env_Bol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_MIDIA'


class BoletosMidiaAux(models.Model):
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol', blank=True, null=True)  # Field name made lowercase.
    parcnf_saida_pagto = models.BigIntegerField(db_column='ParcNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_MIDIA_AUX'


class BoletosMidiaNfe(models.Model):
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol')  # Field name made lowercase.
    data_bol = models.DateTimeField(db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField(db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField(db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField(db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField(db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField(db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField(db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField(db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField(db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField(db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField(db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField(db_column='Env_Bol')  # Field name made lowercase.
    ind_tip_nfe_srv = models.NullBooleanField(db_column='IND_TIP_NFE_SRV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_MIDIA_NFE'


class BoletosMidiaNfeaux(models.Model):
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol', blank=True, null=True)  # Field name made lowercase.
    parcnf_saida_pagto = models.BigIntegerField(db_column='ParcNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    ind_tip_nfe_srv = models.NullBooleanField(db_column='IND_TIP_NFE_SRV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_MIDIA_NFEAUX'


class BoletosTechcd(models.Model):
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol', primary_key=True)  # Field name made lowercase.
    data_bol = models.DateTimeField(db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField(db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField(db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField(db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField(db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField(db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField(db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField(db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField(db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField(db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField(db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField(db_column='Env_Bol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_TECHCD'


class BoletosTechcdNfe(models.Model):
    nnum_bol = models.BigIntegerField(db_column='NNum_Bol', primary_key=True)  # Field name made lowercase.
    data_bol = models.DateTimeField(db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField(db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField(db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField(db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField(db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField(db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField(db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField(db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField(db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField(db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField(db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField(db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField(db_column='Env_Bol')  # Field name made lowercase.
    ind_tip_nfe_srv = models.NullBooleanField(db_column='IND_TIP_NFE_SRV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOLETOS_TECHCD_NFe'


class Bv(models.Model):
    desc_bv = models.CharField(db_column='DESC_BV', max_length=5)  # Field name made lowercase.
    porc_bv = models.IntegerField(db_column='PORC_BV', blank=True, null=True)  # Field name made lowercase.
    porctechcd_bv = models.IntegerField(db_column='PORCTECHCD_BV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BV'


class Bv2(models.Model):
    desc_bv = models.CharField(db_column='DESC_BV', primary_key=True, max_length=5)  # Field name made lowercase.
    porc_bv = models.FloatField(db_column='PORC_BV', blank=True, null=True)  # Field name made lowercase.
    porctechcd_bv = models.FloatField(db_column='PORCTECHCD_BV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BV2'


class Caixas(models.Model):
    cod_caixa = models.BigIntegerField(db_column='COD_CAIXA', primary_key=True)  # Field name made lowercase.
    desc_caixa = models.CharField(db_column='DESC_CAIXA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    volume = models.FloatField(db_column='VOLUME', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    base = models.FloatField(db_column='BASE', blank=True, null=True)  # Field name made lowercase.
    altura = models.FloatField(db_column='ALTURA', blank=True, null=True)  # Field name made lowercase.
    profundidade = models.FloatField(db_column='PROFUNDIDADE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAIXAS'


class Capacidades(models.Model):
    cod_capacidade = models.BigIntegerField()
    desc_capacidade = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CAPACIDADES'


class CapacidadeCategoria(models.Model):
    cod_capacidade = models.BigIntegerField()
    cod_cat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'CAPACIDADE_CATEGORIA'
        unique_together = (('cod_capacidade', 'cod_cat'),)


class CapacidadeCategorias(models.Model):
    cod_capacidade = models.BigIntegerField()
    cod_cat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'CAPACIDADE_CATEGORIAS'


class Categorias(models.Model):
    cod_cat = models.CharField(db_column='COD_CAT', primary_key=True, max_length=5)  # Field name made lowercase.
    desc_cat = models.CharField(db_column='DESC_CAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cod_supercat = models.BigIntegerField(db_column='COD_SUPERCAT', blank=True, null=True)  # Field name made lowercase.
    mostrar_cat = models.CharField(db_column='MOSTRAR_CAT', max_length=17, blank=True, null=True)  # Field name made lowercase.
    apelido_cat = models.CharField(db_column='APELIDO_CAT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORIAS'


class CategoriasRec(models.Model):
    cod_catrec = models.BigIntegerField(db_column='COD_CATREC', primary_key=True)  # Field name made lowercase.
    desc_catrec = models.CharField(db_column='DESC_CATREC', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORIAS_REC'


class CategoriasServ(models.Model):
    cod_catserv = models.CharField(db_column='COD_CATSERV', primary_key=True, max_length=5)  # Field name made lowercase.
    desc_catserv = models.CharField(db_column='DESC_CATSERV', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORIAS_SERV'


class CategoriaSuper(models.Model):
    cod_cat = models.BigIntegerField()
    cod_supercat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'CATEGORIA_SUPER'


class CatDesp(models.Model):
    cod_catdesp = models.BigIntegerField(db_column='COD_CATDESP', primary_key=True)  # Field name made lowercase.
    desc_catdesp = models.CharField(db_column='DESC_CATDESP', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAT_DESP'


class CatForn(models.Model):
    cod_cat = models.CharField(db_column='COD_CAT', max_length=5)  # Field name made lowercase.
    cod_forn = models.BigIntegerField(db_column='COD_FORN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAT_FORN'


class Cep(models.Model):
    faixai_cep = models.BigIntegerField(db_column='FAIXAI_CEP')  # Field name made lowercase.
    faixaf_cep = models.BigIntegerField(db_column='FAIXAF_CEP')  # Field name made lowercase.
    opsedex_cep = models.SmallIntegerField(db_column='OPSEDEX_CEP', blank=True, null=True)  # Field name made lowercase.
    tabpreco_cep = models.CharField(db_column='TABPRECO_CEP', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP'
        unique_together = (('faixai_cep', 'faixaf_cep'),)


class Cep10(models.Model):
    faixai_c10 = models.BigIntegerField(db_column='FAIXAI_C10')  # Field name made lowercase.
    faixaf_c10 = models.BigIntegerField(db_column='FAIXAF_C10')  # Field name made lowercase.
    sedex_c10 = models.SmallIntegerField(db_column='SEDEX_C10', blank=True, null=True)  # Field name made lowercase.
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_10'


class CepConv(models.Model):
    faixai_cco = models.BigIntegerField(db_column='FAIXAI_CCO')  # Field name made lowercase.
    faixaf_cco = models.BigIntegerField(db_column='FAIXAF_CCO')  # Field name made lowercase.
    sedex_cco = models.SmallIntegerField(db_column='SEDEX_CCO', blank=True, null=True)  # Field name made lowercase.
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_CONV'


class CepEncNormal(models.Model):
    cep_ini_cap = models.CharField(db_column='CEP_INI_CAP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cep_fin_cap = models.CharField(db_column='CEP_FIN_CAP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sigla_local = models.CharField(db_column='SIGLA_LOCAL', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_ENC_NORMAL'


class CepEno(models.Model):
    faixai_eno = models.IntegerField(db_column='FAIXAI_ENO', blank=True, null=True)  # Field name made lowercase.
    faixaf_eno = models.IntegerField(db_column='FAIXAF_ENO', blank=True, null=True)  # Field name made lowercase.
    encomenda_eno = models.SmallIntegerField(db_column='ENCOMENDA_ENO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_ENO'


class CepEsedex(models.Model):
    faixai_cep = models.BigIntegerField(db_column='FAIXAI_CEP')  # Field name made lowercase.
    faixaf_cep = models.BigIntegerField(db_column='FAIXAF_CEP')  # Field name made lowercase.
    opsedex_cep = models.IntegerField(db_column='OPSEDEX_CEP', blank=True, null=True)  # Field name made lowercase.
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.
    tabpreco_cep = models.CharField(db_column='TABPRECO_CEP', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_ESEDEX'


class CepExtmotoboy(models.Model):
    faixaini_cep = models.BigIntegerField(db_column='FAIXAINI_CEP', blank=True, null=True)  # Field name made lowercase.
    faixafim_cep = models.BigIntegerField(db_column='FAIXAFIM_CEP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_EXTMOTOBOY'


class CepInsentivoFiscal(models.Model):
    faixai_cep = models.BigIntegerField(db_column='FAIXAI_CEP', blank=True, null=True)  # Field name made lowercase.
    faixaf_cep = models.BigIntegerField(db_column='FAIXAF_CEP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_INSENTIVO_FISCAL'


class CepLaercio(models.Model):
    cep_ini = models.BigIntegerField(db_column='CEP_INI', blank=True, null=True)  # Field name made lowercase.
    cep_fim = models.BigIntegerField(db_column='CEP_FIM', blank=True, null=True)  # Field name made lowercase.
    cod_preco = models.BigIntegerField(db_column='COD_PRECO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_LAERCIO'


class CepLaercioespecial(models.Model):
    cep_field = models.BigIntegerField(db_column='CEP ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bairro = models.CharField(db_column='Bairro', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_LaercioEspecial'


class CepMotoboy(models.Model):
    faixai_mboy = models.BigIntegerField(db_column='FAIXAI_MBOY', primary_key=True)  # Field name made lowercase.
    faixaf_mboy = models.BigIntegerField(db_column='FAIXAF_MBOY')  # Field name made lowercase.
    opcao_mboy = models.IntegerField(db_column='OPCAO_MBOY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_MOTOBOY'


class CepSedexHoje(models.Model):
    localidade_sh = models.CharField(db_column='LOCALIDADE_SH', max_length=30)  # Field name made lowercase.
    faixacep_ini = models.BigIntegerField(db_column='FAIXACEP_INI')  # Field name made lowercase.
    faixacep_fin = models.BigIntegerField(db_column='FAIXACEP_FIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_SEDEX_HOJE'
        unique_together = (('localidade_sh', 'faixacep_ini', 'faixacep_fin'),)


class CepTotal(models.Model):
    cep_ini = models.BigIntegerField(db_column='CEP_INI', blank=True, null=True)  # Field name made lowercase.
    cep_fim = models.BigIntegerField(db_column='CEP_FIM', blank=True, null=True)  # Field name made lowercase.
    cod_preco = models.BigIntegerField(db_column='COD_PRECO', blank=True, null=True)  # Field name made lowercase.
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CEP_TOTAL'


class CfopNfe(models.Model):
    cfop = models.CharField(db_column='CFOP', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ie = models.NullBooleanField(db_column='IE')  # Field name made lowercase.
    sittribut = models.CharField(db_column='SitTribut', max_length=3, blank=True, null=True)  # Field name made lowercase.
    icms = models.NullBooleanField(db_column='ICMS')  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    prod_importado = models.NullBooleanField(db_column='PROD_IMPORTADO')  # Field name made lowercase.
    cod_ct_prod = models.IntegerField(db_column='COD_CT_PROD', blank=True, null=True)  # Field name made lowercase.
    substtributaria = models.NullBooleanField(db_column='SubstTributaria')  # Field name made lowercase.
    base_legal = models.CharField(db_column='BASE_LEGAL', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFOP_NFE'


class ClassificacaoFiscal(models.Model):
    classitrib_prod = models.CharField(max_length=20, blank=True, null=True)
    cod_ct_prod = models.BigIntegerField(db_column='COD_CT_PROD', blank=True, null=True)  # Field name made lowercase.
    cest_prod = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CLASSIFICACAO_FISCAL'


class Clientes(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.IntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contato_cli = models.CharField(db_column='CONTATO_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_cli = models.CharField(db_column='EMAIL_CLI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email2_cli = models.CharField(db_column='EMAIL2_CLI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    end2_cli = models.CharField(db_column='END2_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num2_cli = models.CharField(db_column='NUM2_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair2_cli = models.CharField(db_column='BAIR2_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid2_cli = models.CharField(db_column='CID2_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est2_cli = models.CharField(db_column='EST2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep2_cli = models.CharField(db_column='CEP2_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg_cli = models.CharField(db_column='RG_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ddd2_cli = models.CharField(db_column='DDD2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_cli = models.CharField(db_column='TEL2_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ramal2_cli = models.CharField(db_column='RAMAL2_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dddfax_cli = models.CharField(db_column='DDDFAX_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fax_cli = models.CharField(db_column='FAX_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramalfax_cli = models.CharField(db_column='RAMALFAX_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    obs_cli = models.TextField(db_column='OBS_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_divulg = models.BigIntegerField(db_column='COD_DIVULG', blank=True, null=True)  # Field name made lowercase.
    semacresc_cli = models.NullBooleanField(db_column='SEMACRESC_CLI')  # Field name made lowercase.
    aprazosemnf_cli = models.NullBooleanField(db_column='APRAZOSEMNF_CLI')  # Field name made lowercase.
    precosprom_cli = models.NullBooleanField(db_column='PRECOSPROM_CLI')  # Field name made lowercase.
    email_info_cli = models.NullBooleanField(db_column='EMAIL_INFO_CLI')  # Field name made lowercase.
    dataincl_cli = models.DateTimeField(db_column='DATAINCL_CLI', blank=True, null=True)  # Field name made lowercase.
    nome2_cli = models.CharField(db_column='NOME2_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cpf2_cli = models.CharField(db_column='CPF2_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj2_cli = models.CharField(db_column='CNPJ2_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg2_cli = models.CharField(db_column='RG2_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ie2_cli = models.CharField(db_column='IE2_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    pes2_cli = models.CharField(db_column='PES2_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_at = models.BigIntegerField(db_column='COD_AT', blank=True, null=True)  # Field name made lowercase.
    cod_cre = models.BigIntegerField(db_column='COD_CRE', blank=True, null=True)  # Field name made lowercase.
    valid_cre = models.DateTimeField(db_column='VALID_CRE', blank=True, null=True)  # Field name made lowercase.
    dt_alt_cad = models.DateTimeField(db_column='DT_ALT_CAD', blank=True, null=True)  # Field name made lowercase.
    avisou_exp_cred = models.NullBooleanField(db_column='AVISOU_EXP_CRED')  # Field name made lowercase.
    cargo_conta_cli = models.CharField(db_column='CARGO_CONTA_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    departamento_conta_cli = models.CharField(db_column='DEPARTAMENTO_CONTA_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user_alt_cad = models.CharField(db_column='USER_ALT_CAD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tel_fin_cli = models.CharField(db_column='TEL_FIN_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ddd_fin_cli = models.CharField(db_column='DDD_FIN_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    suframa_cli = models.CharField(db_column='SUFRAMA_CLI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    contato_fin_cli = models.CharField(db_column='CONTATO_FIN_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    bv_cli = models.IntegerField(blank=True, null=True)
    rimage_cli = models.NullBooleanField(db_column='RIMAGE_CLI')  # Field name made lowercase.
    emailnfe_cli = models.CharField(db_column='EmailNFE_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datahab_cli = models.DateTimeField(db_column='dataHab_Cli', blank=True, null=True)  # Field name made lowercase.
    quemhab_cli = models.CharField(db_column='QuemHab_Cli', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES'


class ClientesContrato(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    datault_contr = models.DateTimeField(db_column='DATAULT_CONTR', blank=True, null=True)  # Field name made lowercase.
    userult_contr = models.CharField(db_column='USERULT_CONTR', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_CONTRATO'


class ClientesDatasimport(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    numevent_cli = models.IntegerField(db_column='NUMEVENT_CLI')  # Field name made lowercase.
    mes_cli = models.CharField(db_column='MES_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    evento_cli = models.CharField(db_column='EVENTO_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_DATASIMPORT'
        unique_together = (('cod_cli', 'numevent_cli'),)


class ClientesDesativos(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_DESATIVOS'


class ClientesEndfat(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_ENDFAT'


class ClientesEstrategico(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', primary_key=True)  # Field name made lowercase.
    quemflag = models.CharField(db_column='QUEMFLAG', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_ESTRATEGICO'


class ClientesFeira(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.IntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contato_cli = models.CharField(db_column='CONTATO_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_cli = models.CharField(db_column='EMAIL_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email2_cli = models.CharField(db_column='EMAIL2_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    end2_cli = models.CharField(db_column='END2_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num2_cli = models.CharField(db_column='NUM2_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair2_cli = models.CharField(db_column='BAIR2_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid2_cli = models.CharField(db_column='CID2_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est2_cli = models.CharField(db_column='EST2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep2_cli = models.CharField(db_column='CEP2_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg_cli = models.CharField(db_column='RG_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ddd2_cli = models.CharField(db_column='DDD2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_cli = models.CharField(db_column='TEL2_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal2_cli = models.CharField(db_column='RAMAL2_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dddfax_cli = models.CharField(db_column='DDDFAX_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fax_cli = models.CharField(db_column='FAX_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramalfax_cli = models.CharField(db_column='RAMALFAX_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    obs_cli = models.TextField(db_column='OBS_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_divulg = models.BigIntegerField(db_column='COD_DIVULG', blank=True, null=True)  # Field name made lowercase.
    semacresc_cli = models.NullBooleanField(db_column='SEMACRESC_CLI')  # Field name made lowercase.
    aprazosemnf_cli = models.NullBooleanField(db_column='APRAZOSEMNF_CLI')  # Field name made lowercase.
    precosprom_cli = models.NullBooleanField(db_column='PRECOSPROM_CLI')  # Field name made lowercase.
    email_info_cli = models.NullBooleanField(db_column='EMAIL_INFO_CLI')  # Field name made lowercase.
    dataincl_cli = models.DateTimeField(db_column='DATAINCL_CLI', blank=True, null=True)  # Field name made lowercase.
    nome2_cli = models.CharField(db_column='NOME2_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cpf2_cli = models.CharField(db_column='CPF2_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj2_cli = models.CharField(db_column='CNPJ2_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg2_cli = models.CharField(db_column='RG2_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ie2_cli = models.CharField(db_column='IE2_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    pes2_cli = models.CharField(db_column='PES2_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_at = models.BigIntegerField(db_column='COD_AT', blank=True, null=True)  # Field name made lowercase.
    cod_cre = models.BigIntegerField(db_column='COD_CRE', blank=True, null=True)  # Field name made lowercase.
    valid_cre = models.DateTimeField(db_column='VALID_CRE', blank=True, null=True)  # Field name made lowercase.
    dt_alt_cad = models.DateTimeField(db_column='DT_ALT_CAD', blank=True, null=True)  # Field name made lowercase.
    avisou_exp_cred = models.NullBooleanField(db_column='AVISOU_EXP_CRED')  # Field name made lowercase.
    cargo_conta_cli = models.CharField(db_column='CARGO_CONTA_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    departamento_conta_cli = models.CharField(db_column='DEPARTAMENTO_CONTA_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    user_alt_cad = models.CharField(db_column='USER_ALT_CAD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tel_fin_cli = models.CharField(db_column='TEL_FIN_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd_fin_cli = models.CharField(db_column='DDD_FIN_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_FEIRA'


class ClientesFicaramInativos(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend_ina = models.BigIntegerField(db_column='COD_VEND_INA', blank=True, null=True)  # Field name made lowercase.
    data_ina = models.DateTimeField(db_column='DATA_INA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_FICARAM_INATIVOS'


class ClientesIcms(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_ICMS'


class ClientesIndeterminado(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    data_cre = models.DateTimeField(db_column='DATA_CRE', blank=True, null=True)  # Field name made lowercase.
    cod_cre = models.BigIntegerField(db_column='COD_CRE', blank=True, null=True)  # Field name made lowercase.
    nome_cre = models.CharField(db_column='NOME_CRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valid_cre = models.DateTimeField(db_column='VALID_CRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_INDETERMINADO'


class ClientesIndicacao(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    cod_conta = models.BigIntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    infl_cli = models.BigIntegerField(db_column='INFL_CLI', blank=True, null=True)  # Field name made lowercase.
    tipoinfl_cli = models.CharField(db_column='TIPOINFL_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_INDICACAO'


class ClientesPerfil(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    setor_cli = models.IntegerField(db_column='SETOR_CLI', blank=True, null=True)  # Field name made lowercase.
    ativ_cli = models.IntegerField(db_column='ATIV_CLI', blank=True, null=True)  # Field name made lowercase.
    faixa_cli = models.IntegerField(db_column='FAIXA_CLI', blank=True, null=True)  # Field name made lowercase.
    dtnasc_cli = models.DateTimeField(db_column='DTNASC_CLI', blank=True, null=True)  # Field name made lowercase.
    tipo_cli = models.IntegerField(db_column='TIPO_CLI', blank=True, null=True)  # Field name made lowercase.
    infl_cod = models.BigIntegerField(db_column='INFL_COD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_PERFIL'


class ClientesRelacionados(models.Model):
    cod_cli1 = models.BigIntegerField(db_column='COD_CLI1', blank=True, null=True)  # Field name made lowercase.
    cod_cli2 = models.BigIntegerField(db_column='COD_CLI2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_RELACIONADOS'


class ClientesRimage(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    garantia_cli = models.NullBooleanField(db_column='GARANTIA_CLI')  # Field name made lowercase.
    valgarantia_cli = models.DateTimeField(db_column='VALGARANTIA_CLI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_RIMAGE'


class ClientesSolangeAtivos(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIENTES_SOLANGE_ATIVOS'


class CliComprasCli(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', primary_key=True)  # Field name made lowercase.
    nome_usu = models.CharField(db_column='Nome_Usu', max_length=50)  # Field name made lowercase.
    data_cad = models.DateTimeField(db_column='Data_Cad')  # Field name made lowercase.
    cod_periodicidade = models.ForeignKey('CliComprasPeriodicidade', models.DO_NOTHING, db_column='Cod_Periodicidade')  # Field name made lowercase.
    frequencia = models.IntegerField(db_column='Frequencia')  # Field name made lowercase.
    comp_oito_meses = models.BooleanField(db_column='Comp_oito_meses')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_COMPRAS_CLI'


class CliComprasConc(models.Model):
    cod_conc = models.BigIntegerField(db_column='Cod_Conc', primary_key=True)  # Field name made lowercase.
    desc_conc = models.CharField(db_column='Desc_Conc', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_COMPRAS_CONC'


class CliComprasItmCliConc(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli')  # Field name made lowercase.
    cod_conc = models.ForeignKey(CliComprasConc, models.DO_NOTHING, db_column='Cod_Conc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_COMPRAS_ITM_CLI_CONC'
        unique_together = (('cod_cli', 'cod_conc'),)


class CliComprasItmCliPeriodo(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli')  # Field name made lowercase.
    cod_periodo = models.ForeignKey('CliComprasPeriodo', models.DO_NOTHING, db_column='Cod_Periodo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_COMPRAS_ITM_CLI_PERIODO'
        unique_together = (('cod_cli', 'cod_periodo'),)


class CliComprasPeriodicidade(models.Model):
    cod_periodicidade = models.IntegerField(db_column='Cod_Periodicidade', primary_key=True)  # Field name made lowercase.
    desc_periodicidade = models.CharField(db_column='Desc_Periodicidade', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_COMPRAS_PERIODICIDADE'


class CliComprasPeriodo(models.Model):
    cod_periodo = models.IntegerField(db_column='Cod_Periodo', primary_key=True)  # Field name made lowercase.
    cod_periodicidade = models.ForeignKey(CliComprasPeriodicidade, models.DO_NOTHING, db_column='Cod_Periodicidade', blank=True, null=True)  # Field name made lowercase.
    desc_periodo = models.CharField(db_column='Desc_Periodo', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_COMPRAS_PERIODO'


class CliCredito(models.Model):
    cod_cred = models.BigIntegerField(db_column='Cod_Cred', primary_key=True)  # Field name made lowercase.
    desc_cred = models.CharField(db_column='Desc_Cred', max_length=50, blank=True, null=True)  # Field name made lowercase.
    val_cred = models.FloatField(db_column='Val_Cred', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_CREDITO'


class CliFretefixo(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', primary_key=True)  # Field name made lowercase.
    frete = models.DecimalField(db_column='Frete', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_FRETEFIXO'


class CliRemNf(models.Model):
    cod_nf_saida = models.ForeignKey('NotasFiscais', models.DO_NOTHING, db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_nf_rem = models.BigIntegerField(db_column='COD_NF_REM', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_REM_NF'


class CliVerificaSintegra(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    tiposint_cli = models.CharField(db_column='TIPOSINT_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    datasint_cli = models.DateTimeField(db_column='DATASINT_CLI', blank=True, null=True)  # Field name made lowercase.
    enviou_email = models.NullBooleanField(db_column='ENVIOU_EMAIL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLI_VERIFICA_SINTEGRA'


class CmpNf(models.Model):
    cod_cmp = models.ForeignKey('PedCompra', models.DO_NOTHING, db_column='Cod_Cmp')  # Field name made lowercase.
    cod_nf_entrada = models.BigIntegerField(db_column='Cod_NF_Entrada')  # Field name made lowercase.
    ativ_cmp_nf = models.BooleanField(db_column='Ativ_Cmp_NF')  # Field name made lowercase.
    empresa_cmp_nf = models.CharField(db_column='Empresa_CMP_NF', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMP_NF'


class CmpNfServ(models.Model):
    cod_cmp_serv = models.ForeignKey('PedCompraServ', models.DO_NOTHING, db_column='Cod_Cmp_Serv')  # Field name made lowercase.
    cod_nf_entrada = models.BigIntegerField(db_column='Cod_NF_Entrada')  # Field name made lowercase.
    ativ_cmp_nf = models.BooleanField(db_column='Ativ_Cmp_NF')  # Field name made lowercase.
    empresa_cmp_nf = models.CharField(db_column='Empresa_CMP_NF', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CMP_NF_SERV'


class Codebar(models.Model):
    val_ascii = models.BigIntegerField(db_column='VAL_ASCII', blank=True, null=True)  # Field name made lowercase.
    val_verifica = models.BigIntegerField(db_column='VAL_VERIFICA', blank=True, null=True)  # Field name made lowercase.
    caractere = models.CharField(db_column='CARACTERE', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CODEBAR'


class Comissao(models.Model):
    cod_func = models.ForeignKey('Funcionarios', models.DO_NOTHING, db_column='COD_FUNC', primary_key=True)  # Field name made lowercase.
    porc_comiss = models.FloatField(db_column='PORC_COMISS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMISSAO'


class Conferencia(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    data_conf = models.DateTimeField(db_column='DATA_CONF', blank=True, null=True)  # Field name made lowercase.
    conferido = models.NullBooleanField(db_column='CONFERIDO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFERENCIA'


class Configuracoes(models.Model):
    resp_os = models.CharField(db_column='RESP_OS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resp_etq = models.CharField(db_column='RESP_ETQ', max_length=90, blank=True, null=True)  # Field name made lowercase.
    resp_cmp = models.CharField(db_column='RESP_CMP', max_length=90, blank=True, null=True)  # Field name made lowercase.
    resp_pgto = models.CharField(db_column='RESP_PGTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resp_fat = models.CharField(db_column='RESP_FAT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resp_pre = models.CharField(db_column='RESP_PRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cam_foto = models.CharField(db_column='CAM_FOTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mintabvenda = models.IntegerField(db_column='MINTABVENDA', blank=True, null=True)  # Field name made lowercase.
    mincustomedio = models.IntegerField(db_column='MINCUSTOMEDIO', blank=True, null=True)  # Field name made lowercase.
    maxnumparc = models.IntegerField(db_column='MAXNUMPARC', blank=True, null=True)  # Field name made lowercase.
    porcacresc = models.IntegerField(db_column='PORCACRESC', blank=True, null=True)  # Field name made lowercase.
    nome_empr = models.CharField(db_column='NOME_EMPR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ende_empr = models.CharField(db_column='ENDE_EMPR', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ie_empr = models.CharField(db_column='IE_EMPR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnpj_empr = models.CharField(db_column='CNPJ_EMPR', max_length=18, blank=True, null=True)  # Field name made lowercase.
    tele_empr = models.CharField(db_column='TELE_EMPR', max_length=9, blank=True, null=True)  # Field name made lowercase.
    email_empr = models.CharField(db_column='EMAIL_EMPR', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_empr = models.CharField(db_column='CEP_EMPR', max_length=9, blank=True, null=True)  # Field name made lowercase.
    bairro_empr = models.CharField(db_column='BAIRRO_EMPR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidade_empr = models.CharField(db_column='CIDADE_EMPR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    uf_empr = models.CharField(db_column='UF_EMPR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    site_empr = models.CharField(db_column='SITE_EMPR', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dias_acresc = models.IntegerField(db_column='DIAS_ACRESC', blank=True, null=True)  # Field name made lowercase.
    valor_cartareg = models.DecimalField(db_column='VALOR_CARTAREG', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porc_emba = models.FloatField(db_column='PORC_EMBA', blank=True, null=True)  # Field name made lowercase.
    val_iss = models.IntegerField(db_column='VAL_ISS', blank=True, null=True)  # Field name made lowercase.
    custo_frete = models.FloatField(db_column='CUSTO_FRETE', blank=True, null=True)  # Field name made lowercase.
    imp_prod = models.CharField(db_column='IMP_PROD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imp_serv = models.CharField(db_column='IMP_SERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    imp_bol = models.CharField(db_column='IMP_BOL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    juros_boleto = models.IntegerField(db_column='JUROS_BOLETO', blank=True, null=True)  # Field name made lowercase.
    porta_serv_torp = models.IntegerField(db_column='PORTA_SERV_TORP', blank=True, null=True)  # Field name made lowercase.
    limite_ref_pf = models.DecimalField(db_column='LIMITE_REF_PF', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    email_cr = models.DateTimeField(db_column='EMAIL_CR', blank=True, null=True)  # Field name made lowercase.
    email_monitora = models.DateTimeField(db_column='EMAIL_MONITORA', blank=True, null=True)  # Field name made lowercase.
    email_inativo = models.DateTimeField(db_column='EMAIL_INATIVO', blank=True, null=True)  # Field name made lowercase.
    email_senha = models.DateTimeField(db_column='EMAIL_SENHA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIGURACOES'


class ConfMailCredCli(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', blank=True, null=True)  # Field name made lowercase.
    data_envio = models.DateTimeField(db_column='Data_Envio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONF_MAIL_CRED_CLI'


class Contador(models.Model):
    passagens = models.IntegerField(db_column='Passagens', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTADOR'


class ContasPagar(models.Model):
    cod_pagar = models.BigIntegerField(db_column='COD_PAGAR')  # Field name made lowercase.
    cod_desp = models.ForeignKey('Despesas', models.DO_NOTHING, db_column='COD_DESP')  # Field name made lowercase.
    cod_pagto = models.ForeignKey('TipoPagto', models.DO_NOTHING, db_column='COD_PAGTO')  # Field name made lowercase.
    cod_frmpagto = models.ForeignKey('FormaPagto', models.DO_NOTHING, db_column='COD_FRMPAGTO')  # Field name made lowercase.
    cod_banco = models.ForeignKey(Bancos, models.DO_NOTHING, db_column='COD_BANCO')  # Field name made lowercase.
    datavenc_pagar = models.DateTimeField(db_column='DATAVENC_PAGAR', blank=True, null=True)  # Field name made lowercase.
    valorprev_pagar = models.DecimalField(db_column='VALORPREV_PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorreal_pagar = models.DecimalField(db_column='VALORREAL_PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dataquit_pagar = models.DateTimeField(db_column='DATAQUIT_PAGAR', blank=True, null=True)  # Field name made lowercase.
    quemquit_pagar = models.CharField(db_column='QUEMQUIT_PAGAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numcheque_pagar = models.CharField(db_column='NUMCHEQUE_PAGAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numdoc_pagar = models.CharField(db_column='NUMDOC_PAGAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    obs_pagar = models.TextField(db_column='OBS_PAGAR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTAS_PAGAR'
        unique_together = (('cod_pagar', 'cod_desp', 'cod_pagto', 'cod_frmpagto', 'cod_banco'),)


class ContasPagarData(models.Model):
    cod_pagar = models.BigIntegerField(db_column='COD_PAGAR')  # Field name made lowercase.
    cod_desp = models.BigIntegerField(db_column='COD_DESP')  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO')  # Field name made lowercase.
    cod_frmpagto = models.BigIntegerField(db_column='COD_FRMPAGTO')  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO')  # Field name made lowercase.
    datavenc_pagar = models.DateTimeField(db_column='DATAVENC_PAGAR', blank=True, null=True)  # Field name made lowercase.
    valorprev_pagar = models.DecimalField(db_column='VALORPREV_PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorreal_pagar = models.DecimalField(db_column='VALORREAL_PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dataquit_pagar = models.DateTimeField(db_column='DATAQUIT_PAGAR', blank=True, null=True)  # Field name made lowercase.
    quemquit_pagar = models.CharField(db_column='QUEMQUIT_PAGAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numcheque_pagar = models.CharField(db_column='NUMCHEQUE_PAGAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numdoc_pagar = models.CharField(db_column='NUMDOC_PAGAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    obs_pagar = models.TextField(db_column='OBS_PAGAR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTAS_PAGAR_DATA'


class ContasPagarMidia(models.Model):
    cod_pagar = models.BigIntegerField(db_column='COD_PAGAR')  # Field name made lowercase.
    cod_desp = models.BigIntegerField(db_column='COD_DESP')  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO')  # Field name made lowercase.
    cod_frmpagto = models.BigIntegerField(db_column='COD_FRMPAGTO')  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO')  # Field name made lowercase.
    datavenc_pagar = models.DateTimeField(db_column='DATAVENC_PAGAR', blank=True, null=True)  # Field name made lowercase.
    valorprev_pagar = models.DecimalField(db_column='VALORPREV_PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valorreal_pagar = models.DecimalField(db_column='VALORREAL_PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dataquit_pagar = models.DateTimeField(db_column='DATAQUIT_PAGAR', blank=True, null=True)  # Field name made lowercase.
    quemquit_pagar = models.CharField(db_column='QUEMQUIT_PAGAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    numcheque_pagar = models.CharField(db_column='NUMCHEQUE_PAGAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    numdoc_pagar = models.CharField(db_column='NUMDOC_PAGAR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    obs_pagar = models.TextField(db_column='OBS_PAGAR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTAS_PAGAR_MIDIA'


class ContasReceber(models.Model):
    cod_receb = models.BigIntegerField(db_column='COD_RECEB', primary_key=True)  # Field name made lowercase.
    cod_receita = models.ForeignKey('Receitas', models.DO_NOTHING, db_column='COD_RECEITA', blank=True, null=True)  # Field name made lowercase.
    valor_receb = models.DecimalField(db_column='VALOR_RECEB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dataquit_receb = models.DateTimeField(db_column='DATAQUIT_RECEB', blank=True, null=True)  # Field name made lowercase.
    quemquit_receb = models.CharField(db_column='QUEMQUIT_RECEB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.ForeignKey(Bancos, models.DO_NOTHING, db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTAS_RECEBER'


class ContatosCli(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    cod_conta = models.BigIntegerField(db_column='COD_CONTA')  # Field name made lowercase.
    nome_conta = models.CharField(db_column='NOME_CONTA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_conta = models.CharField(db_column='EMAIL_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email2_conta = models.CharField(db_column='EMAIL2_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddd_conta = models.CharField(db_column='DDD_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_conta = models.CharField(db_column='TEL_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ramal_conta = models.CharField(db_column='RAMAL_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cargo_conta = models.CharField(db_column='CARGO_CONTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    departamento_conta = models.CharField(db_column='DEPARTAMENTO_CONTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    receber_email = models.NullBooleanField(db_column='RECEBER_EMAIL')  # Field name made lowercase.
    dddcel_conta = models.CharField(db_column='DDDCEL_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cel_conta = models.CharField(db_column='CEL_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ddd2_conta = models.CharField(db_column='DDD2_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_conta = models.CharField(db_column='TEL2_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ramal2_conta = models.CharField(db_column='RAMAL2_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    niver_conta = models.CharField(db_column='NIVER_CONTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ativo_conta = models.NullBooleanField(db_column='ATIVO_CONTA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTATOS_CLI'
        unique_together = (('cod_cli', 'cod_conta'),)


class ContatosCliBkp(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    cod_conta = models.BigIntegerField(db_column='COD_CONTA')  # Field name made lowercase.
    nome_conta = models.CharField(db_column='NOME_CONTA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_conta = models.CharField(db_column='EMAIL_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email2_conta = models.CharField(db_column='EMAIL2_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddd_conta = models.CharField(db_column='DDD_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_conta = models.CharField(db_column='TEL_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal_conta = models.CharField(db_column='RAMAL_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cargo_conta = models.CharField(db_column='CARGO_CONTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    departamento_conta = models.CharField(db_column='DEPARTAMENTO_CONTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    receber_email = models.NullBooleanField(db_column='RECEBER_EMAIL')  # Field name made lowercase.
    dddcel_conta = models.CharField(db_column='DDDCEL_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cel_conta = models.CharField(db_column='CEL_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd2_conta = models.CharField(db_column='DDD2_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_conta = models.CharField(db_column='TEL2_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal2_conta = models.CharField(db_column='RAMAL2_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    niver_conta = models.CharField(db_column='NIVER_CONTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ativo_conta = models.NullBooleanField(db_column='ATIVO_CONTA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTATOS_CLI_BKP'


class ContatosPros(models.Model):
    cod_pros = models.ForeignKey('Telemarketing', models.DO_NOTHING, db_column='COD_PROS')  # Field name made lowercase.
    cod_conta = models.BigIntegerField(db_column='COD_CONTA')  # Field name made lowercase.
    nome_conta = models.CharField(db_column='NOME_CONTA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_conta = models.CharField(db_column='EMAIL_CONTA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email2_conta = models.CharField(db_column='EMAIL2_CONTA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ddd_conta = models.CharField(db_column='DDD_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_conta = models.CharField(db_column='TEL_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal_conta = models.CharField(db_column='RAMAL_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTATOS_PROS'
        unique_together = (('cod_pros', 'cod_conta'),)


class Contrato(models.Model):
    cod_contrato = models.BigAutoField(db_column='COD_CONTRATO', primary_key=True)  # Field name made lowercase.
    num_contrato = models.CharField(db_column='NUM_CONTRATO', max_length=11)  # Field name made lowercase.
    empresa = models.CharField(db_column='EMPRESA', max_length=1)  # Field name made lowercase.
    data_criacao = models.DateTimeField(db_column='DATA_CRIACAO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTRATO'


class ContratoCliente(models.Model):
    cod_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='COD_CONTRATO')  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTRATO_CLIENTE'
        unique_together = (('cod_contrato', 'cod_cli'),)


class ControleEntregas(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', primary_key=True)  # Field name made lowercase.
    dest_ctr = models.IntegerField(db_column='DEST_CTR', blank=True, null=True)  # Field name made lowercase.
    tipodest_ctr = models.CharField(db_column='TIPODEST_CTR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retirapagto_ctr = models.BooleanField(db_column='RETIRAPAGTO_CTR')  # Field name made lowercase.
    prazo_ctr = models.IntegerField(db_column='PRAZO_CTR', blank=True, null=True)  # Field name made lowercase.
    dtprevist_ctr = models.DateTimeField(db_column='DTPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist_ctr = models.DateTimeField(db_column='HRPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist2_ctr = models.DateTimeField(db_column='HRPREVIST2_CTR', blank=True, null=True)  # Field name made lowercase.
    val_ctr = models.DecimalField(db_column='VAL_CTR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_ctr = models.TextField(db_column='OBS_CTR', blank=True, null=True)  # Field name made lowercase.
    pto_ref = models.CharField(db_column='PTO_REF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paga_frete = models.NullBooleanField(db_column='PAGA_FRETE')  # Field name made lowercase.
    val_frete = models.DecimalField(db_column='VAL_FRETE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_ctr = models.SmallIntegerField(db_column='CANC_CTR', blank=True, null=True)  # Field name made lowercase.
    cod_mboy = models.BigIntegerField(db_column='COD_MBOY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROLE_ENTREGAS'


class ControleEntregasAvulso(models.Model):
    cod_ctr = models.BigIntegerField(db_column='COD_CTR', primary_key=True)  # Field name made lowercase.
    cod_func = models.IntegerField(db_column='COD_FUNC', blank=True, null=True)  # Field name made lowercase.
    dest_ctr = models.IntegerField(db_column='DEST_CTR', blank=True, null=True)  # Field name made lowercase.
    cod_conta = models.IntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    tipodest_ctr = models.CharField(db_column='TIPODEST_CTR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    retirapagto_ctr = models.BooleanField(db_column='RETIRAPAGTO_CTR')  # Field name made lowercase.
    prazo_ctr = models.IntegerField(db_column='PRAZO_CTR', blank=True, null=True)  # Field name made lowercase.
    dtprevist_ctr = models.DateTimeField(db_column='DTPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist_ctr = models.DateTimeField(db_column='HRPREVIST_CTR', blank=True, null=True)  # Field name made lowercase.
    hrprevist2_ctr = models.DateTimeField(db_column='HRPREVIST2_CTR', blank=True, null=True)  # Field name made lowercase.
    val_ctr = models.DecimalField(db_column='VAL_CTR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_ctr = models.TextField(db_column='OBS_CTR', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.IntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    pto_ref = models.CharField(db_column='PTO_REF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    paga_frete = models.NullBooleanField(db_column='PAGA_FRETE')  # Field name made lowercase.
    canc_ctr = models.SmallIntegerField(db_column='CANC_CTR', blank=True, null=True)  # Field name made lowercase.
    val_frete = models.DecimalField(db_column='VAL_FRETE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_mboy = models.SmallIntegerField(db_column='COD_MBOY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROLE_ENTREGAS_AVULSO'


class ControleEtiquetaCorreios(models.Model):
    cod_srv_ect = models.IntegerField(db_column='COD_SRV_ECT')  # Field name made lowercase.
    cod_obj_ect = models.CharField(db_column='COD_OBJ_ECT', max_length=13)  # Field name made lowercase.
    des_srv_ect = models.CharField(db_column='DES_SRV_ECT', max_length=50)  # Field name made lowercase.
    dth_cri_etq = models.DateTimeField(db_column='DTH_CRI_ETQ')  # Field name made lowercase.
    ind_sta_uso = models.BooleanField(db_column='IND_STA_USO')  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTROLE_ETIQUETA_CORREIOS'
        unique_together = (('cod_srv_ect', 'cod_obj_ect'),)


class CorpoNfSaida(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='Cod_NF_Saida', primary_key=True)  # Field name made lowercase.
    corpo_nf_saida = models.TextField(db_column='Corpo_NF_Saida')  # Field name made lowercase. This field type is a guess.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CORPO_NF_SAIDA'


class Caminhoversao(models.Model):
    path = models.CharField(db_column='Path', max_length=200)  # Field name made lowercase.
    path2 = models.CharField(db_column='Path2', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CaminhoVersao'


class ClientesEntespecial(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes_EntEspecial'


class ClientesHistcontatos(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', blank=True, null=True)  # Field name made lowercase.
    datahist_cli = models.DateTimeField(db_column='Datahist_Cli', blank=True, null=True)  # Field name made lowercase.
    usuario_cli = models.CharField(db_column='Usuario_Cli', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acontecimento_cli = models.TextField(db_column='Acontecimento_Cli', blank=True, null=True)  # Field name made lowercase.
    proxcontato_cli = models.DateTimeField(db_column='ProxContato_Cli', blank=True, null=True)  # Field name made lowercase.
    envemail_cli = models.NullBooleanField(db_column='EnvEmail_Cli')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes_HistContatos'


class ClientesRepresentante(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clientes_Representante'


class Code128(models.Model):
    ascii = models.FloatField(db_column='Ascii', blank=True, null=True)  # Field name made lowercase.
    char = models.CharField(db_column='Char', max_length=255, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Code128'


class Code128C(models.Model):
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    char = models.CharField(db_column='Char', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Code128C'


class ColetaOs(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='Cod_Os', primary_key=True)  # Field name made lowercase.
    num_coleta = models.CharField(db_column='Num_Coleta', max_length=10, blank=True, null=True)  # Field name made lowercase.
    data_coleta = models.DateTimeField(db_column='Data_Coleta', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coleta_OS'


class DatasCom(models.Model):
    dia = models.IntegerField(blank=True, null=True)
    mes = models.IntegerField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DATAS_COM'


class DependentesFunc(models.Model):
    cod_func = models.ForeignKey('Funcionarios', models.DO_NOTHING, db_column='Cod_Func')  # Field name made lowercase.
    nome_depend = models.CharField(db_column='Nome_Depend', max_length=40)  # Field name made lowercase.
    idade_depend = models.IntegerField(db_column='Idade_Depend', blank=True, null=True)  # Field name made lowercase.
    data_nasc_depend = models.DateTimeField(db_column='Data_Nasc_Depend')  # Field name made lowercase.
    grau_parent_depend = models.CharField(db_column='Grau_Parent_Depend', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPENDENTES_FUNC'
        unique_together = (('cod_func', 'nome_depend', 'data_nasc_depend'),)


class Deposito(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    user_mov = models.CharField(db_column='USER_MOV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tipo_mov = models.CharField(db_column='TIPO_MOV', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPOSITO'


class Despesas(models.Model):
    cod_desp = models.BigIntegerField(db_column='COD_DESP', primary_key=True)  # Field name made lowercase.
    desc_desp = models.CharField(db_column='DESC_DESP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_conta = models.IntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    tipo_desp = models.CharField(db_column='TIPO_DESP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_catdesp = models.ForeignKey(CatDesp, models.DO_NOTHING, db_column='COD_CATDESP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DESPESAS'


class DetalhesAmostra(models.Model):
    cod_requis = models.BigIntegerField(db_column='COD_REQUIS', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.BigIntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    data_entrega = models.DateTimeField(db_column='DATA_ENTREGA', blank=True, null=True)  # Field name made lowercase.
    cod_func = models.BigIntegerField(db_column='COD_FUNC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DETALHES_AMOSTRA'


class DevolucaoOs(models.Model):
    cod_dev = models.BigIntegerField(db_column='Cod_Dev', primary_key=True)  # Field name made lowercase.
    data_dev = models.DateTimeField(db_column='Data_Dev', blank=True, null=True)  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    valor_dev = models.DecimalField(db_column='Valor_Dev', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_dev = models.TextField(db_column='OBS_DEV', blank=True, null=True)  # Field name made lowercase.
    resp_dev = models.CharField(db_column='Resp_DEV', max_length=30, blank=True, null=True)  # Field name made lowercase.
    status_dev = models.CharField(db_column='STATUS_DEV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    autorizada_dev = models.NullBooleanField(db_column='AUTORIZADA_DEV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEVOLUCAO_OS'


class Divulgacao(models.Model):
    cod_divulg = models.BigIntegerField(db_column='COD_DIVULG', primary_key=True)  # Field name made lowercase.
    desc_divulg = models.CharField(db_column='DESC_DIVULG', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIVULGACAO'


class Emails(models.Model):
    cod_mail = models.BigIntegerField(db_column='COD_MAIL', primary_key=True)  # Field name made lowercase.
    nome_mail = models.CharField(db_column='NOME_MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_mail = models.CharField(db_column='PES_MAIL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contato_mail = models.CharField(db_column='CONTATO_MAIL', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_mail = models.CharField(db_column='EMAIL_MAIL', max_length=61, blank=True, null=True)  # Field name made lowercase.
    ddd_mail = models.CharField(db_column='DDD_MAIL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_mail = models.CharField(db_column='TEL_MAIL', max_length=9, blank=True, null=True)  # Field name made lowercase.
    opiniao_site_mail = models.TextField(db_column='OPINIAO_SITE_MAIL', blank=True, null=True)  # Field name made lowercase.
    cod_divulg = models.IntegerField(db_column='COD_DIVULG', blank=True, null=True)  # Field name made lowercase.
    dataincl_mail = models.DateTimeField(db_column='DATAINCL_MAIL', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.IntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    informativo = models.NullBooleanField(db_column='INFORMATIVO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMAILS'


class Embalagem(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    embal_peso = models.FloatField(db_column='EMBAL_PESO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMBALAGEM'
        unique_together = (('faixai_peso', 'faixaf_peso'),)


class EmbalagemTechcd(models.Model):
    cod_caixa = models.BigIntegerField(db_column='COD_CAIXA', primary_key=True)  # Field name made lowercase.
    base_caixa = models.FloatField(db_column='BASE_CAIXA', blank=True, null=True)  # Field name made lowercase.
    altura_caixa = models.FloatField(db_column='ALTURA_CAIXA', blank=True, null=True)  # Field name made lowercase.
    largura_caixa = models.FloatField(db_column='LARGURA_CAIXA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMBALAGEM_TECHCD'


class EncomendaNormal(models.Model):
    peso_ini = models.FloatField(db_column='PESO_INI', blank=True, null=True)  # Field name made lowercase.
    peso_fin = models.FloatField(db_column='PESO_FIN', blank=True, null=True)  # Field name made lowercase.
    valor_cap = models.DecimalField(db_column='VALOR_CAP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valor_int = models.DecimalField(db_column='VALOR_INT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sigla_local = models.ForeignKey('LocalidadeEncNormal', models.DO_NOTHING, db_column='SIGLA_LOCAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENCOMENDA_NORMAL'


class EncNormal(models.Model):
    faixai_peso = models.IntegerField(db_column='FAIXAI_PESO', blank=True, null=True)  # Field name made lowercase.
    faixaf_peso = models.IntegerField(db_column='FAIXAF_PESO', blank=True, null=True)  # Field name made lowercase.
    estado_eno = models.DecimalField(db_column='ESTADO_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprrjsc_eno = models.DecimalField(db_column='MGPRRJSC_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprrjsc_int_eno = models.DecimalField(db_column='MGPRRJSC_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs_eno = models.DecimalField(db_column='DFESGOMSRS_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs_int_eno = models.DecimalField(db_column='DFESGOMSRS_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bamtto_eno = models.DecimalField(db_column='BAMTTO_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bamtto_int_eno = models.DecimalField(db_column='BAMTTO_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alse_eno = models.DecimalField(db_column='ALSE_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alse_int_eno = models.DecimalField(db_column='ALSE_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cemapbpepirnro_eno = models.DecimalField(db_column='CEMAPBPEPIRNRO_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cemapbpepirnro_int_eno = models.DecimalField(db_column='CEMAPBPEPIRNRO_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acappa_eno = models.DecimalField(db_column='ACAPPA_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acappa_int_eno = models.DecimalField(db_column='ACAPPA_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    am_eno = models.DecimalField(db_column='AM_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    am_int_eno = models.DecimalField(db_column='AM_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rr_eno = models.DecimalField(db_column='RR_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rr_int_eno = models.DecimalField(db_column='RR_INT_ENO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENC_NORMAL'


class EnderecoEntregas(models.Model):
    cod_end = models.BigAutoField(db_column='Cod_End', primary_key=True)  # Field name made lowercase.
    nome_end = models.CharField(db_column='Nome_End', max_length=30, blank=True, null=True)  # Field name made lowercase.
    contato_end = models.CharField(db_column='Contato_End', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ddd_end = models.CharField(db_column='DDD_End', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_end = models.CharField(db_column='Tel_End', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ramal_end = models.CharField(db_column='Ramal_End', max_length=10, blank=True, null=True)  # Field name made lowercase.
    end_end = models.CharField(db_column='End_End', max_length=50, blank=True, null=True)  # Field name made lowercase.
    comp_end = models.CharField(db_column='Comp_End', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cid_end = models.CharField(db_column='Cid_End', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair_end = models.CharField(db_column='Bair_End', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cep_end = models.CharField(db_column='Cep_End', max_length=9, blank=True, null=True)  # Field name made lowercase.
    uf_end = models.CharField(db_column='UF_End', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENDERECO_ENTREGAS'


class Entregas(models.Model):
    cod_ent = models.BigIntegerField(db_column='COD_ENT', primary_key=True)  # Field name made lowercase.
    desc_ent = models.CharField(db_column='DESC_ENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prazo_ent = models.CharField(db_column='PRAZO_ENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    obs_ent = models.TextField(db_column='OBS_ENT', blank=True, null=True)  # Field name made lowercase.
    fat_ent = models.BooleanField(db_column='FAT_ENT')  # Field name made lowercase.
    tabcor_ent = models.BooleanField(db_column='TABCOR_ENT')  # Field name made lowercase.
    form_ent = models.BooleanField(db_column='FORM_ENT')  # Field name made lowercase.
    contato_ent = models.CharField(db_column='CONTATO_ENT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ddd1_ent = models.CharField(db_column='DDD1_ENT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_ent = models.CharField(db_column='TEL1_ENT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ramal1_ent = models.CharField(db_column='RAMAL1_ENT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    end_ent = models.CharField(db_column='END_ENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cid_ent = models.CharField(db_column='CID_ENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_ent = models.CharField(db_column='EST_ENT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cnpj_ent = models.CharField(db_column='CNPJ_ENT', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_ent = models.CharField(db_column='IE_ENT', max_length=19, blank=True, null=True)  # Field name made lowercase.
    mostra_ent = models.NullBooleanField(db_column='MOSTRA_ENT')  # Field name made lowercase.
    transpor_ent = models.NullBooleanField(db_column='TRANSPOR_ENT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENTREGAS'


class Esedex(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    valsta_sed = models.DecimalField(db_column='VALSTA_SED', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valpri_sed = models.DecimalField(db_column='VALPRI_SED', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valexp_sed = models.DecimalField(db_column='VALEXP_SED', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valconv_sed = models.DecimalField(db_column='VALCONV_SED', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    outsta_sed = models.DecimalField(db_column='OUTSTA_SED', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    outconv_sed = models.DecimalField(db_column='OUTCONV_SED', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESEDEX'
        unique_together = (('faixai_peso', 'faixaf_peso'),)


class Esedex2(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    valsta_sed2 = models.DecimalField(db_column='VALSTA_SED2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESEDEX2'
        unique_together = (('faixai_peso', 'faixaf_peso'),)


class Esedex3(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    valsta_sed3 = models.DecimalField(db_column='VALSTA_SED3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESEDEX3'
        unique_together = (('faixai_peso', 'faixaf_peso'),)


class Esedex4(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    valsta_sed4 = models.DecimalField(db_column='VALSTA_SED4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESEDEX4'
        unique_together = (('faixai_peso', 'faixaf_peso'),)


class EmailErros(models.Model):
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigo = models.BigIntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tabela = models.CharField(db_column='Tabela', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Email_Erros'


class EmailErrosGlobal(models.Model):
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arquivo = models.CharField(db_column='Arquivo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    codigo = models.BigIntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=80, blank=True, null=True)  # Field name made lowercase.
    tabela = models.CharField(db_column='Tabela', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Email_Erros_Global'


class EmailFiesp(models.Model):
    codigo = models.BigIntegerField(db_column='Codigo')  # Field name made lowercase.
    email_fiesp = models.CharField(db_column='Email_FIESP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    enviar = models.NullBooleanField(db_column='Enviar')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Email_FIESP'


class EmailInformativo(models.Model):
    col001 = models.CharField(db_column='Col001', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Email_Informativo'


class EmailNfe(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_env = models.DateTimeField(db_column='DATA_ENV', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email_cli = models.CharField(db_column='Email_Cli', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Email_NFe'


class Emailsnaoenviados(models.Model):
    mail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EmailsNaoEnviados'


class EmbalagemCorrecao(models.Model):
    faixai_peso = models.IntegerField(db_column='FaixaI_Peso', blank=True, null=True)  # Field name made lowercase.
    faixaf_peso = models.IntegerField(db_column='FaixaF_Peso', blank=True, null=True)  # Field name made lowercase.
    fator_correcao = models.FloatField(db_column='Fator_Correcao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Embalagem_Correcao'


class Fluxocaixa(models.Model):
    data = models.DateTimeField(db_column='DATA', primary_key=True)  # Field name made lowercase.
    receber = models.DecimalField(db_column='RECEBER', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pagar = models.DecimalField(db_column='PAGAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FLUXOCAIXA'


class FormaPagto(models.Model):
    cod_frmpagto = models.BigIntegerField(db_column='COD_FRMPAGTO', primary_key=True)  # Field name made lowercase.
    desc_frmpagto = models.CharField(db_column='DESC_FRMPAGTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dias_frmpagto = models.IntegerField(db_column='DIAS_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORMA_PAGTO'


class Fornecedores(models.Model):
    cod_forn = models.BigIntegerField(db_column='COD_FORN', primary_key=True)  # Field name made lowercase.
    nome_forn = models.CharField(db_column='NOME_FORN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contato_forn = models.CharField(db_column='CONTATO_FORN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email_forn = models.CharField(db_column='EMAIL_FORN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_forn = models.TextField(db_column='END_FORN', blank=True, null=True)  # Field name made lowercase.
    num_forn = models.CharField(db_column='NUM_FORN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_forn = models.CharField(db_column='BAIR_FORN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_forn = models.CharField(db_column='CID_FORN', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_forn = models.CharField(db_column='EST_FORN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_forn = models.CharField(db_column='CEP_FORN', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cnpj_forn = models.CharField(db_column='CNPJ_FORN', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_forn = models.CharField(db_column='IE_FORN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ddd1_forn = models.CharField(db_column='DDD1_FORN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_forn = models.CharField(db_column='TEL1_FORN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ramal1_forn = models.CharField(db_column='RAMAL1_FORN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ddd2_forn = models.CharField(db_column='DDD2_FORN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_forn = models.CharField(db_column='TEL2_FORN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ramal2_forn = models.CharField(db_column='RAMAL2_FORN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dddfax_forn = models.CharField(db_column='DDDFAX_FORN', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fax_forn = models.CharField(db_column='FAX_FORN', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramalfax_forn = models.CharField(db_column='RAMALFAX_FORN', max_length=10, blank=True, null=True)  # Field name made lowercase.
    obs_forn = models.TextField(db_column='OBS_FORN', blank=True, null=True)  # Field name made lowercase.
    site_forn = models.TextField(db_column='SITE_FORN', blank=True, null=True)  # Field name made lowercase.
    dolar_forn = models.NullBooleanField(db_column='DOLAR_FORN')  # Field name made lowercase.
    cod_pais = models.IntegerField(db_column='COD_PAIS')  # Field name made lowercase.
    comp_forn = models.CharField(db_column='COMP_FORN', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORNECEDORES'


class FornProd(models.Model):
    cod_forn = models.ForeignKey(Fornecedores, models.DO_NOTHING, db_column='COD_FORN')  # Field name made lowercase.
    cod_prod = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='COD_PROD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FORN_PROD'
        unique_together = (('cod_forn', 'cod_prod'),)


class Frases(models.Model):
    cod_frase = models.IntegerField(db_column='Cod_Frase')  # Field name made lowercase.
    desc_frase = models.CharField(db_column='Desc_Frase', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRASES'


class FreteRegiao(models.Model):
    cod_ent = models.ForeignKey(Entregas, models.DO_NOTHING, db_column='COD_ENT')  # Field name made lowercase.
    sigla_regiao = models.CharField(db_column='SIGLA_REGIAO', max_length=3)  # Field name made lowercase.
    desc_destino = models.CharField(db_column='DESC_DESTINO', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRETE_REGIAO'
        unique_together = (('cod_ent', 'sigla_regiao'),)


class FreteValor(models.Model):
    cod_ent = models.ForeignKey(FreteRegiao, models.DO_NOTHING, db_column='COD_ENT')  # Field name made lowercase.
    sigla_regiao = models.ForeignKey(FreteRegiao, models.DO_NOTHING, db_column='SIGLA_REGIAO')  # Field name made lowercase.
    peso_ini = models.BigIntegerField(db_column='PESO_INI')  # Field name made lowercase.
    peso_fim = models.BigIntegerField(db_column='PESO_FIM')  # Field name made lowercase.
    frete_valor = models.DecimalField(db_column='FRETE_VALOR', max_digits=19, decimal_places=4)  # Field name made lowercase.
    frete_taxa = models.DecimalField(db_column='FRETE_TAXA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    taxa_excedente = models.DecimalField(db_column='TAXA_EXCEDENTE', max_digits=19, decimal_places=4)  # Field name made lowercase.
    taxa_despacho = models.DecimalField(db_column='TAXA_DESPACHO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxa_pedagio = models.DecimalField(db_column='TAXA_PEDAGIO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    max_peso_pedagio = models.DecimalField(db_column='MAX_PESO_PEDAGIO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    taxa_gris = models.DecimalField(db_column='TAXA_GRIS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FRETE_VALOR'
        unique_together = (('cod_ent', 'sigla_regiao', 'peso_ini', 'peso_fim'),)


class Funcionarios(models.Model):
    cod_func = models.BigIntegerField(db_column='COD_FUNC', primary_key=True)  # Field name made lowercase.
    nome_func = models.CharField(db_column='NOME_FUNC', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nomecomp_func = models.CharField(db_column='NOMECOMP_FUNC', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cargo_func = models.CharField(db_column='CARGO_FUNC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    email_func = models.CharField(db_column='EMAIL_FUNC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tel_func = models.CharField(db_column='TEL_FUNC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    tel2_func = models.CharField(db_column='TEL2_FUNC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    end_func = models.CharField(db_column='END_FUNC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_func = models.CharField(db_column='NUM_FUNC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_func = models.CharField(db_column='BAIR_FUNC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_func = models.CharField(db_column='CID_FUNC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_func = models.CharField(db_column='EST_FUNC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_func = models.CharField(db_column='CEP_FUNC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    obs_func = models.TextField(db_column='OBS_FUNC', blank=True, null=True)  # Field name made lowercase.
    aniv_func = models.DateTimeField(db_column='ANIV_FUNC', blank=True, null=True)  # Field name made lowercase.
    cargo2_func = models.CharField(db_column='CARGO2_FUNC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ctps_func = models.CharField(db_column='CTPS_FUNC', max_length=16, blank=True, null=True)  # Field name made lowercase.
    rg_func = models.CharField(db_column='RG_FUNC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pis_func = models.CharField(db_column='PIS_FUNC', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cpf_func = models.CharField(db_column='CPF_FUNC', max_length=14, blank=True, null=True)  # Field name made lowercase.
    estciv_func = models.CharField(db_column='ESTCIV_FUNC', max_length=11, blank=True, null=True)  # Field name made lowercase.
    dataadm_func = models.DateTimeField(db_column='DATAADM_FUNC', blank=True, null=True)  # Field name made lowercase.
    datadem_func = models.DateTimeField(db_column='DATADEM_FUNC', blank=True, null=True)  # Field name made lowercase.
    numdepend_func = models.IntegerField(db_column='NUMDEPEND_FUNC', blank=True, null=True)  # Field name made lowercase.
    salario_func = models.DecimalField(db_column='SALARIO_FUNC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    receber_email = models.NullBooleanField(db_column='RECEBER_EMAIL')  # Field name made lowercase.
    codbarras_func = models.CharField(db_column='CODBARRAS_FUNC', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FUNCIONARIOS'


class GrupoProdutos(models.Model):
    cod_grupo = models.BigIntegerField(db_column='COD_GRUPO', primary_key=True)  # Field name made lowercase.
    desc_grupo = models.CharField(db_column='DESC_GRUPO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apelido_grupo = models.CharField(db_column='APELIDO_GRUPO', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GRUPO_PRODUTOS'


class GrupoUsuarios(models.Model):
    cod_grupo = models.BigIntegerField(blank=True, null=True)
    desc_grupo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GRUPO_USUARIOS'


class HistoricoMinimos(models.Model):
    cod_prod = models.BigIntegerField()
    min_anterior = models.BigIntegerField(blank=True, null=True)
    min_atual = models.BigIntegerField(blank=True, null=True)
    total_saida = models.BigIntegerField(blank=True, null=True)
    total_entrada = models.BigIntegerField(blank=True, null=True)
    data_alteracao = models.DateTimeField()
    hora_alteracao = models.CharField(max_length=20)
    cod_hist = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'HISTORICO_MINIMOS'
        unique_together = (('cod_prod', 'data_alteracao', 'hora_alteracao', 'cod_hist'),)


class HistManutencao(models.Model):
    cod_solicitacao = models.BigIntegerField(db_column='COD_SOLICITACAO', blank=True, null=True)  # Field name made lowercase.
    datahist_sol = models.DateTimeField(db_column='DATAHIST_SOL', blank=True, null=True)  # Field name made lowercase.
    userhist_sol = models.CharField(db_column='USERHIST_SOL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aconthist_sol = models.TextField(db_column='ACONTHIST_SOL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HIST_MANUTENCAO'


class HistRma(models.Model):
    cod_rma = models.BigIntegerField(db_column='COD_RMA', blank=True, null=True)  # Field name made lowercase.
    datahist_rma = models.DateTimeField(db_column='DATAHIST_RMA', blank=True, null=True)  # Field name made lowercase.
    usuario_rma = models.CharField(db_column='USUARIO_RMA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    acontecimento_rma = models.TextField(db_column='ACONTECIMENTO_RMA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HIST_RMA'


class IbptImposto(models.Model):
    codigo = models.TextField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ex = models.TextField(db_column='EX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tabela = models.TextField(db_column='TABELA', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    federal_nac = models.TextField(db_column='FEDERAL_NAC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    federal_imp = models.TextField(db_column='FEDERAL_IMP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estadual = models.TextField(db_column='ESTADUAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    municipal = models.TextField(db_column='MUNICIPAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    versao = models.TextField(db_column='VERSAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_ini = models.TextField(db_column='DT_INI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_fim = models.TextField(db_column='DT_FIM', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'IBPT_IMPOSTO'


class Icms(models.Model):
    desc_icms = models.CharField(db_column='DESC_ICMS', primary_key=True, max_length=2)  # Field name made lowercase.
    val_icms = models.IntegerField(db_column='VAL_ICMS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ICMS'


class IcmsstAnteriormente(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    baseicmsst_nf_saida = models.DecimalField(db_column='BASEICMSST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icmsst_nf_saida = models.DecimalField(db_column='ICMSST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_nf_entrada = models.TextField(db_column='COD_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ICMSST_ANTERIORMENTE'


class IcmsSt(models.Model):
    codigo = models.BigAutoField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    icms_st = models.FloatField(db_column='ICMS_ST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ICMS_ST'


class IcmsSubs(models.Model):
    cod_nf_saida = models.ForeignKey('NotasFiscais', models.DO_NOTHING, db_column='COD_NF_SAIDA', unique=True, blank=True, null=True)  # Field name made lowercase.
    base_calc_icms_sub = models.DecimalField(db_column='BASE_CALC_ICMS_SUB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valor_icms_sub = models.DecimalField(db_column='VALOR_ICMS_SUB', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ICMS_SUBS'


class ImpostosCorreios(models.Model):
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.
    desc_imp = models.CharField(db_column='DESC_IMP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    porc_imp = models.BigIntegerField(db_column='PORC_IMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMPOSTOS_CORREIOS'


class ImpostoIbpt(models.Model):
    codigo = models.BigIntegerField(db_column='CODIGO')  # Field name made lowercase.
    ex = models.IntegerField(db_column='EX', blank=True, null=True)  # Field name made lowercase.
    tabela = models.IntegerField(db_column='TABELA', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aliqnac = models.DecimalField(db_column='ALIQNAC', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aliqimp = models.DecimalField(db_column='ALIQIMP', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    versao = models.CharField(db_column='VERSAO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dt_inclusao = models.DateTimeField(db_column='DT_INCLUSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMPOSTO_IBPT'


class Indicacao(models.Model):
    cod_indic = models.BigIntegerField(db_column='COD_INDIC')  # Field name made lowercase.
    nome_indic = models.CharField(db_column='NOME_INDIC', max_length=40, blank=True, null=True)  # Field name made lowercase.
    contato_indic = models.CharField(db_column='CONTATO_INDIC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ddd_indic = models.CharField(db_column='DDD_INDIC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_indic = models.CharField(db_column='TEL_INDIC', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal_indic = models.CharField(db_column='RAMAL_INDIC', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INDICACAO'


class Inventario(models.Model):
    cod_invent = models.BigIntegerField(db_column='COD_INVENT')  # Field name made lowercase.
    data_invent = models.DateTimeField(db_column='DATA_INVENT')  # Field name made lowercase.
    justif_invent = models.TextField(db_column='JUSTIF_INVENT')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'INVENTARIO'


class InventarioMovimentacao(models.Model):
    cod_invent = models.BigIntegerField(db_column='COD_INVENT', blank=True, null=True)  # Field name made lowercase.
    data_invent = models.DateTimeField(db_column='DATA_INVENT', blank=True, null=True)  # Field name made lowercase.
    user_invent = models.CharField(db_column='USER_INVENT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    qtdetech_invent = models.BigIntegerField(db_column='QTDETECH_INVENT', blank=True, null=True)  # Field name made lowercase.
    teoricotech_invent = models.BigIntegerField(db_column='TEORICOTECH_INVENT', blank=True, null=True)  # Field name made lowercase.
    qtdedata_invent = models.BigIntegerField(db_column='QTDEDATA_INVENT', blank=True, null=True)  # Field name made lowercase.
    teoricodata_invent = models.BigIntegerField(db_column='TEORICODATA_INVENT', blank=True, null=True)  # Field name made lowercase.
    qtdemidia_invent = models.BigIntegerField(db_column='QTDEMIDIA_INVENT', blank=True, null=True)  # Field name made lowercase.
    teoricomidia_invent = models.BigIntegerField(db_column='TEORICOMIDIA_INVENT', blank=True, null=True)  # Field name made lowercase.
    saldotech_mov = models.BigIntegerField(db_column='SALDOTECH_MOV', blank=True, null=True)  # Field name made lowercase.
    saldodata_mov = models.BigIntegerField(db_column='SALDODATA_MOV', blank=True, null=True)  # Field name made lowercase.
    saldomidia_mov = models.BigIntegerField(db_column='SALDOMIDIA_MOV', blank=True, null=True)  # Field name made lowercase.
    motivo_invent = models.TextField(db_column='MOTIVO_INVENT', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVENTARIO_MOVIMENTACAO'


class IsentastCli(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    quemisent_cli = models.CharField(db_column='QUEMISENT_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dataisent_cli = models.DateTimeField(db_column='DATAISENT_CLI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ISENTAST_CLI'


class ItmAtualizacoes(models.Model):
    cod_alt = models.BigIntegerField(db_column='COD_ALT', blank=True, null=True)  # Field name made lowercase.
    usuario_viu = models.CharField(db_column='USUARIO_VIU', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_ATUALIZACOES'


class ItmClicontrato(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV', blank=True, null=True)  # Field name made lowercase.
    valor_contr = models.DecimalField(db_column='VALOR_CONTR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CLICONTRATO'


class ItmClirimage(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV', blank=True, null=True)  # Field name made lowercase.
    qtde_cli = models.BigIntegerField(db_column='QTDE_CLI', blank=True, null=True)  # Field name made lowercase.
    valor_cli = models.DecimalField(db_column='VALOR_CLI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CLIRIMAGE'


class ItmClirimageHist(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    data_hist = models.DateTimeField(db_column='DATA_HIST', blank=True, null=True)  # Field name made lowercase.
    usuario_hist = models.CharField(db_column='USUARIO_HIST', max_length=30, blank=True, null=True)  # Field name made lowercase.
    acontecimento_hist = models.TextField(db_column='ACONTECIMENTO_HIST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CLIRIMAGE_HIST'


class ItmCmp(models.Model):
    cod_cmp = models.ForeignKey('PedCompra', models.DO_NOTHING, db_column='COD_CMP')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    qtde_cmp = models.FloatField(db_column='QTDE_CMP', blank=True, null=True)  # Field name made lowercase.
    valor_cmp = models.DecimalField(db_column='VALOR_CMP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_cmp = models.FloatField(db_column='IPI_CMP', blank=True, null=True)  # Field name made lowercase.
    receb_cmp = models.IntegerField(db_column='RECEB_CMP', blank=True, null=True)  # Field name made lowercase.
    gerou_cr = models.NullBooleanField(db_column='GEROU_CR')  # Field name made lowercase.
    base_ipi = models.DecimalField(db_column='BASE_IPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CMP'
        unique_together = (('cod_cmp', 'cod_prod'),)


class ItmCmpPagto(models.Model):
    cod_cmp = models.ForeignKey('PedCompra', models.DO_NOTHING, db_column='COD_CMP')  # Field name made lowercase.
    parcnum_cmp = models.IntegerField(db_column='PARCNUM_CMP')  # Field name made lowercase.
    cod_pagto = models.ForeignKey('TipoPagto', models.DO_NOTHING, db_column='COD_PAGTO')  # Field name made lowercase.
    cod_frmpagto = models.ForeignKey(FormaPagto, models.DO_NOTHING, db_column='COD_FRMPAGTO')  # Field name made lowercase.
    val_pagto = models.DecimalField(db_column='VAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavenc_cmp = models.DateTimeField(db_column='DATAVENC_CMP', blank=True, null=True)  # Field name made lowercase.
    nf_cmp = models.BigIntegerField(db_column='NF_CMP', blank=True, null=True)  # Field name made lowercase.
    quit_cmp = models.NullBooleanField(db_column='QUIT_CMP')  # Field name made lowercase.
    quemquit_cmp = models.CharField(db_column='QUEMQUIT_CMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dataquit_cmp = models.DateTimeField(db_column='DATAQUIT_CMP', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CMP_PAGTO'
        unique_together = (('cod_cmp', 'parcnum_cmp'),)


class ItmCmpServ(models.Model):
    cod_cmp = models.ForeignKey('PedCompraServ', models.DO_NOTHING, db_column='COD_CMP')  # Field name made lowercase.
    cod_serv_presta = models.ForeignKey('ServPrestaServ', models.DO_NOTHING, db_column='COD_SERV_PRESTA')  # Field name made lowercase.
    qtde_cmp = models.IntegerField(db_column='QTDE_CMP', blank=True, null=True)  # Field name made lowercase.
    valor_cmp = models.DecimalField(db_column='VALOR_CMP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_ipi = models.DecimalField(db_column='BASE_IPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CMP_SERV'
        unique_together = (('cod_cmp', 'cod_serv_presta'),)


class ItmCmpServPagto(models.Model):
    cod_cmp = models.BigIntegerField(db_column='COD_CMP')  # Field name made lowercase.
    parcnum_cmp = models.IntegerField(db_column='PARCNUM_CMP')  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO')  # Field name made lowercase.
    cod_frmpagto = models.BigIntegerField(db_column='COD_FRMPAGTO')  # Field name made lowercase.
    val_pagto = models.DecimalField(db_column='VAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavenc_cmp = models.DateTimeField(db_column='DATAVENC_CMP', blank=True, null=True)  # Field name made lowercase.
    quit_cmp = models.NullBooleanField(db_column='QUIT_CMP')  # Field name made lowercase.
    quemquit_cmp = models.CharField(db_column='QUEMQUIT_CMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dataquit_cmp = models.DateTimeField(db_column='DATAQUIT_CMP', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CMP_SERV_PAGTO'
        unique_together = (('cod_cmp', 'parcnum_cmp'),)


class ItmConferencia(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde_conf = models.IntegerField(db_column='QTDE_CONF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_CONFERENCIA'


class ItmDetAmostra(models.Model):
    cod_requis = models.BigIntegerField(db_column='COD_REQUIS')  # Field name made lowercase.
    num_amostra = models.IntegerField(db_column='NUM_AMOSTRA')  # Field name made lowercase.
    arq_producao = models.CharField(db_column='ARQ_PRODUCAO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    arq_viewer = models.CharField(db_column='ARQ_VIEWER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    num_cores = models.IntegerField(db_column='NUM_CORES', blank=True, null=True)  # Field name made lowercase.
    data_disponivel_prod = models.DateTimeField(db_column='DATA_DISPONIVEL_PROD', blank=True, null=True)  # Field name made lowercase.
    data_aprov_amostra = models.DateTimeField(db_column='DATA_APROV_AMOSTRA', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    data_impressao = models.DateTimeField(db_column='DATA_IMPRESSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_DET_AMOSTRA'
        unique_together = (('cod_requis', 'num_amostra'),)


class ItmDevolucaoOs(models.Model):
    cod_dev = models.ForeignKey(DevolucaoOs, models.DO_NOTHING, db_column='Cod_Dev', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='Cod_Prod', blank=True, null=True)  # Field name made lowercase.
    qtde_prod = models.IntegerField(db_column='QTDE_Prod', blank=True, null=True)  # Field name made lowercase.
    qtde_devolvida = models.IntegerField(db_column='QTDE_DEVOLVIDA', blank=True, null=True)  # Field name made lowercase.
    qtde_voltou_etq = models.IntegerField(db_column='QTDE_Voltou_ETQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_DEVOLUCAO_OS'


class ItmEntregas(models.Model):
    cod_ent = models.ForeignKey(Entregas, models.DO_NOTHING, db_column='COD_ENT')  # Field name made lowercase.
    estatend_ent = models.CharField(db_column='ESTATEND_ENT', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_ENTREGAS'
        unique_together = (('cod_ent', 'estatend_ent'),)


class ItmNfeSaida(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frete_nf_saida = models.DecimalField(db_column='FRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_saida = models.DecimalField(db_column='DESCONTO_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.FloatField(db_column='PIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_saida = models.FloatField(db_column='COFINS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.FloatField(db_column='IPI_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_saida = models.DecimalField(db_column='VALORIPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_saida = models.FloatField(db_column='ST_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    substtributaria_nf_saida = models.DecimalField(db_column='SUBSTTRIBUTARIA_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_saida = models.DecimalField(db_column='BASEST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA'


class ItmNfeSaidaData(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frete_nf_saida = models.DecimalField(db_column='FRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_saida = models.DecimalField(db_column='DESCONTO_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.FloatField(db_column='PIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_saida = models.FloatField(db_column='COFINS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.FloatField(db_column='IPI_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_saida = models.DecimalField(db_column='VALORIPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_saida = models.FloatField(db_column='ST_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    substtributaria_nf_saida = models.DecimalField(db_column='SUBSTTRIBUTARIA_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_saida = models.DecimalField(db_column='BASEST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_DATA'


class ItmNfeSaidaDataSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frete_nf_saida = models.DecimalField(db_column='FRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_saida = models.DecimalField(db_column='DESCONTO_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.FloatField(db_column='PIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_saida = models.FloatField(db_column='COFINS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.FloatField(db_column='IPI_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_saida = models.DecimalField(db_column='VALORIPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_saida = models.FloatField(db_column='ST_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    substtributaria_nf_saida = models.DecimalField(db_column='SUBSTTRIBUTARIA_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_saida = models.DecimalField(db_column='BASEST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_DATA_SRV'


class ItmNfeSaidaMidia(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frete_nf_saida = models.DecimalField(db_column='FRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_saida = models.DecimalField(db_column='DESCONTO_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.FloatField(db_column='PIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_saida = models.FloatField(db_column='COFINS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.FloatField(db_column='IPI_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_saida = models.DecimalField(db_column='VALORIPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_saida = models.FloatField(db_column='ST_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    substtributaria_nf_saida = models.DecimalField(db_column='SUBSTTRIBUTARIA_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_saida = models.DecimalField(db_column='BASEST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_MIDIA'


class ItmNfeSaidaMidiaSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frete_nf_saida = models.DecimalField(db_column='FRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_saida = models.DecimalField(db_column='DESCONTO_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.FloatField(db_column='PIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_saida = models.FloatField(db_column='COFINS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.FloatField(db_column='IPI_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_saida = models.DecimalField(db_column='VALORIPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_saida = models.FloatField(db_column='ST_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    substtributaria_nf_saida = models.DecimalField(db_column='SUBSTTRIBUTARIA_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_saida = models.DecimalField(db_column='BASEST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_MIDIA_SRV'


class ItmNfeSaidaPagto(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO'


class ItmNfeSaidaPagtoData(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_DATA'


class ItmNfeSaidaPagtoDataSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_DATA_SRV'


class ItmNfeSaidaPagtoMidia(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_MIDIA'


class ItmNfeSaidaPagtoMidiaSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_MIDIA_SRV'


class ItmNfeSaidaPagtoSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_SRV'


class ItmNfeSaidaSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    frete_nf_saida = models.DecimalField(db_column='FRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_saida = models.DecimalField(db_column='DESCONTO_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.FloatField(db_column='PIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_saida = models.FloatField(db_column='COFINS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.FloatField(db_column='IPI_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_saida = models.DecimalField(db_column='VALORIPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_saida = models.FloatField(db_column='ST_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    substtributaria_nf_saida = models.DecimalField(db_column='SUBSTTRIBUTARIA_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_saida = models.DecimalField(db_column='BASEST_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_SRV'


class ItmNfDev(models.Model):
    cod_nf_dev = models.BigIntegerField(db_column='COD_NF_DEV', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV', blank=True, null=True)  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_DEV'


class ItmNfDevolCli(models.Model):
    cod_devol_cli = models.ForeignKey('NfDevolCli', models.DO_NOTHING, db_column='COD_DEVOL_CLI')  # Field name made lowercase.
    cod_prod = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='COD_PROD')  # Field name made lowercase.
    qtde_devol_cli = models.IntegerField(db_column='QTDE_DEVOL_CLI', blank=True, null=True)  # Field name made lowercase.
    val_devol_cli = models.DecimalField(db_column='VAL_DEVOL_CLI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_DEVOL_CLI'
        unique_together = (('cod_devol_cli', 'cod_prod'),)


class ItmNfDevolForn(models.Model):
    cod_devol_forn = models.ForeignKey('NfDevolForn', models.DO_NOTHING, db_column='COD_DEVOL_FORN')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    qtde_devol_forn = models.IntegerField(db_column='QTDE_DEVOL_FORN', blank=True, null=True)  # Field name made lowercase.
    val_devol_forn = models.DecimalField(db_column='VAL_DEVOL_FORN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_DEVOL_FORN'
        unique_together = (('cod_devol_forn', 'cod_prod'),)


class ItmNfDevPagto(models.Model):
    cod_nf_dev = models.BigIntegerField(db_column='COD_NF_DEV', blank=True, null=True)  # Field name made lowercase.
    parcnf_saida_pagto = models.BigIntegerField(db_column='PARCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_DEV_PAGTO'


class ItmNfEntrada(models.Model):
    cod_nf_entrada = models.ForeignKey('NotasFiscaisEntrada', models.DO_NOTHING, db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_entrada = models.IntegerField(db_column='QTDE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    val_nf_entrada = models.DecimalField(db_column='VAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_entrada = models.FloatField(db_column='ICMS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_entrada = models.FloatField(db_column='IPI_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    bcicmsst_nf_entrada = models.DecimalField(db_column='BCICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtdenfsaida_nf_entrada = models.BigIntegerField(db_column='QTDENFSAIDA_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ENTRADA'
        unique_together = (('cod_nf_entrada', 'cod_prod', 'cod_serv'),)


class ItmNfEntradaData(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_entrada = models.IntegerField(db_column='QTDE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    val_nf_entrada = models.DecimalField(db_column='VAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_entrada = models.FloatField(db_column='ICMS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_entrada = models.FloatField(db_column='IPI_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    bcicmsst_nf_entrada = models.DecimalField(db_column='BCICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtdenfsaida_nf_entrada = models.BigIntegerField(db_column='QTDENFSAIDA_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ENTRADA_DATA'


class ItmNfEntradaMidia(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_entrada = models.IntegerField(db_column='QTDE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    val_nf_entrada = models.DecimalField(db_column='VAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_entrada = models.FloatField(db_column='ICMS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    ipi_nf_entrada = models.FloatField(db_column='IPI_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    bcicmsst_nf_entrada = models.DecimalField(db_column='BCICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    qtdenfsaida_nf_entrada = models.BigIntegerField(db_column='QTDENFSAIDA_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ENTRADA_MIDIA'


class ItmNfEntradaPagto(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_parc = models.IntegerField(db_column='COD_PARC')  # Field name made lowercase.
    val_parc = models.DecimalField(db_column='VAL_PARC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.IntegerField(db_column='TIPO_PAGTO', blank=True, null=True)  # Field name made lowercase.
    forma_pagto = models.IntegerField(db_column='FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    venc_parc = models.DateTimeField(db_column='VENC_PARC', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quit_nf = models.NullBooleanField(db_column='QUIT_NF')  # Field name made lowercase.
    quemquit_nf = models.CharField(db_column='QUEMQUIT_NF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataquit_nf = models.DateTimeField(db_column='DATAQUIT_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ENTRADA_PAGTO'
        unique_together = (('cod_nf_entrada', 'cod_parc'),)


class ItmNfEntradaPagtoData(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_parc = models.IntegerField(db_column='COD_PARC')  # Field name made lowercase.
    val_parc = models.DecimalField(db_column='VAL_PARC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.IntegerField(db_column='TIPO_PAGTO', blank=True, null=True)  # Field name made lowercase.
    forma_pagto = models.IntegerField(db_column='FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    venc_parc = models.DateTimeField(db_column='VENC_PARC', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quit_nf = models.NullBooleanField(db_column='QUIT_NF')  # Field name made lowercase.
    quemquit_nf = models.CharField(db_column='QUEMQUIT_NF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataquit_nf = models.DateTimeField(db_column='DATAQUIT_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ENTRADA_PAGTO_DATA'


class ItmNfEntradaPagtoMidia(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_parc = models.IntegerField(db_column='COD_PARC')  # Field name made lowercase.
    val_parc = models.DecimalField(db_column='VAL_PARC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.IntegerField(db_column='TIPO_PAGTO', blank=True, null=True)  # Field name made lowercase.
    forma_pagto = models.IntegerField(db_column='FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    venc_parc = models.DateTimeField(db_column='VENC_PARC', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quit_nf = models.NullBooleanField(db_column='QUIT_NF')  # Field name made lowercase.
    quemquit_nf = models.CharField(db_column='QUEMQUIT_NF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataquit_nf = models.DateTimeField(db_column='DATAQUIT_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ENTRADA_PAGTO_MIDIA'


class ItmNfIcms(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='Cod_NF_Saida', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_ICMS'


class ItmNfSaida(models.Model):
    cod_nf_saida = models.ForeignKey('NotasFiscais', models.DO_NOTHING, db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA'
        unique_together = (('cod_nf_saida', 'cod_prod', 'cod_serv', 'qtde_nf_saida'),)


class ItmNfSaidaData(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA_DATA'


class ItmNfSaidaIpi(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    valor_ipi = models.DecimalField(db_column='VALOR_IPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA_IPI'


class ItmNfSaidaMidia(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_saida = models.IntegerField(db_column='QTDE_NF_SAIDA')  # Field name made lowercase.
    valor_nf_saida = models.DecimalField(db_column='VALOR_NF_SAIDA', max_digits=19, decimal_places=4)  # Field name made lowercase.
    icms_nf_saida = models.IntegerField(db_column='ICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cf_nf_saida = models.CharField(db_column='CF_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA_MIDIA'


class ItmNfSaidaPagto(models.Model):
    cod_nf_saida = models.ForeignKey('NotasFiscais', models.DO_NOTHING, db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA_PAGTO'
        unique_together = (('cod_nf_saida', 'parcnf_saida_pagto'),)


class ItmNfSaidaPagtoData(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA_PAGTO_DATA'


class ItmNfSaidaPagtoMidia(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    parcnf_saida_pagto = models.DecimalField(db_column='PARCNF_SAIDA_PAGTO', max_digits=19, decimal_places=4)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valnf_saida_pagto = models.DecimalField(db_column='VALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    realnf_saida_pagto = models.DecimalField(db_column='REALNF_SAIDA_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavencnf_saida_pagto = models.DateTimeField(db_column='DATAVENCNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    dataquitnf_saida_pagto = models.DateTimeField(db_column='DATAQUITNF_SAIDA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    quemquitnf_saida_pagto = models.CharField(db_column='QUEMQUITNF_SAIDA_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chqnf_saida_pagto = models.CharField(db_column='CHQNF_SAIDA_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NF_SAIDA_PAGTO_MIDIA'


class ItmNfeEntradaData(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_entrada = models.IntegerField(db_column='QTDE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    val_nf_entrada = models.DecimalField(db_column='VAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_nf_entrada = models.DecimalField(db_column='FRETE_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_entrada = models.DecimalField(db_column='DESCONTO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_entrada = models.DecimalField(db_column='ST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_entrada = models.DecimalField(db_column='BASEST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_entrada = models.FloatField(db_column='IPI_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_entrada = models.DecimalField(db_column='VALORIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_entrada = models.FloatField(db_column='ICMS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cfop_nf_entrada = models.CharField(db_column='CFOP_NF_ENTRADA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sittribut_nf_entrada = models.CharField(db_column='SITTRIBUT_NF_ENTRADA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pis_nf_entrada = models.FloatField(db_column='PIS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_entrada = models.FloatField(db_column='COFINS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    iss_nf_entrada = models.FloatField(db_column='ISS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    base_ipi = models.DecimalField(db_column='BASE_IPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valor_nf_prod = models.DecimalField(db_column='VALOR_NF_PROD', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFe_ENTRADA_DATA'


class ItmNfeEntradaMidia(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_entrada = models.IntegerField(db_column='QTDE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    val_nf_entrada = models.DecimalField(db_column='VAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_nf_entrada = models.DecimalField(db_column='FRETE_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_entrada = models.DecimalField(db_column='DESCONTO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_entrada = models.DecimalField(db_column='ST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_entrada = models.DecimalField(db_column='BASEST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_entrada = models.FloatField(db_column='IPI_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_entrada = models.DecimalField(db_column='VALORIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_entrada = models.FloatField(db_column='ICMS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cfop_nf_entrada = models.CharField(db_column='CFOP_NF_ENTRADA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sittribut_nf_entrada = models.CharField(db_column='SITTRIBUT_NF_ENTRADA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pis_nf_entrada = models.FloatField(db_column='PIS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_entrada = models.FloatField(db_column='COFINS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    iss_nf_entrada = models.FloatField(db_column='ISS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    base_ipi = models.CharField(db_column='BASE_IPI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    valor_nf_prod = models.DecimalField(db_column='VALOR_NF_PROD', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFe_ENTRADA_midia'


class ItmNfeEntradaPagtoData(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_parc = models.IntegerField(db_column='COD_PARC')  # Field name made lowercase.
    val_parc = models.DecimalField(db_column='VAL_PARC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.IntegerField(db_column='TIPO_PAGTO', blank=True, null=True)  # Field name made lowercase.
    forma_pagto = models.IntegerField(db_column='FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    venc_parc = models.DateTimeField(db_column='VENC_PARC', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quit_nf = models.NullBooleanField(db_column='QUIT_NF')  # Field name made lowercase.
    quemquit_nf = models.CharField(db_column='QUEMQUIT_NF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataquit_nf = models.DateTimeField(db_column='DATAQUIT_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFe_ENTRADA_pagto_DATA'


class ItmNfeEntradaPagtoMidia(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_parc = models.IntegerField(db_column='COD_PARC')  # Field name made lowercase.
    val_parc = models.DecimalField(db_column='VAL_PARC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.IntegerField(db_column='TIPO_PAGTO', blank=True, null=True)  # Field name made lowercase.
    forma_pagto = models.IntegerField(db_column='FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    venc_parc = models.DateTimeField(db_column='VENC_PARC', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quit_nf = models.NullBooleanField(db_column='QUIT_NF')  # Field name made lowercase.
    quemquit_nf = models.CharField(db_column='QUEMQUIT_NF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataquit_nf = models.DateTimeField(db_column='DATAQUIT_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_NFe_ENTRADA_pagto_midia'


class ItmOrca(models.Model):
    cod_orca = models.ForeignKey('Orcamentos', models.DO_NOTHING, db_column='COD_ORCA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_orca = models.BigIntegerField(db_column='QTDE_ORCA')  # Field name made lowercase.
    valor_orca = models.DecimalField(db_column='VALOR_ORCA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_ORCA'


class ItmOrcaEmba(models.Model):
    cod_orca = models.ForeignKey('Orcamentos', models.DO_NOTHING, db_column='COD_ORCA')  # Field name made lowercase.
    cod_caixa = models.ForeignKey(EmbalagemTechcd, models.DO_NOTHING, db_column='COD_CAIXA')  # Field name made lowercase.
    qtde_caixa = models.IntegerField(db_column='QTDE_CAIXA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_ORCA_EMBA'
        unique_together = (('cod_orca', 'cod_caixa'),)


class ItmOs(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_os = models.FloatField(db_column='QTDE_OS', blank=True, null=True)  # Field name made lowercase.
    valor_os = models.DecimalField(db_column='VALOR_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    trocavend_os = models.IntegerField(db_column='TROCAVEND_OS', blank=True, null=True)  # Field name made lowercase.
    trocaetq_os = models.IntegerField(db_column='TROCAETQ_OS', blank=True, null=True)  # Field name made lowercase.
    desconto_os = models.FloatField(db_column='DESCONTO_OS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS'
        unique_together = (('cod_os', 'cod_prod', 'cod_serv'),)


class ItmOsAutPagtoMenor(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', primary_key=True)  # Field name made lowercase.
    data_aut = models.DateTimeField(db_column='Data_Aut', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_AUT_PAGTO_MENOR'


class ItmOsCanc(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    cod_motcanc = models.ForeignKey('MotivosCanc', models.DO_NOTHING, db_column='Cod_MotCanc', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_CANC'


class ItmOsCancProd(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    data_canc = models.DateTimeField(db_column='DATA_CANC', blank=True, null=True)  # Field name made lowercase.
    canc_prod = models.NullBooleanField(db_column='CANC_PROD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_CANC_PROD'


class ItmOsCorreios(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    numcorr_os = models.CharField(db_column='NUMCORR_OS', max_length=30)  # Field name made lowercase.
    valorcorr_os = models.DecimalField(db_column='VALORCORR_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesocorr_os = models.FloatField(db_column='PESOCORR_OS', blank=True, null=True)  # Field name made lowercase.
    pesotechcd_os = models.FloatField(db_column='PESOTECHCD_OS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_CORREIOS'
        unique_together = (('cod_os', 'numcorr_os'),)


class ItmOsDatacapt(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', primary_key=True)  # Field name made lowercase.
    id_capt = models.CharField(db_column='ID_Capt', max_length=50)  # Field name made lowercase.
    parcnum_os = models.IntegerField(db_column='ParcNum_OS')  # Field name made lowercase.
    data_capt = models.DateTimeField(db_column='Data_Capt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DATACAPT'


class ItmOsDetfinal(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS', primary_key=True)  # Field name made lowercase.
    datasai_os = models.DateTimeField(db_column='DATASAI_OS', blank=True, null=True)  # Field name made lowercase.
    cod_libera = models.ForeignKey(Funcionarios, models.DO_NOTHING, db_column='COD_LIBERA', blank=True, null=True)  # Field name made lowercase.
    obsfinal_os = models.TextField(db_column='OBSFINAL_OS', blank=True, null=True)  # Field name made lowercase.
    libera_tudo = models.NullBooleanField(db_column='LIBERA_TUDO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DETFINAL'


class ItmOsDetfinalConf(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    cod_conf = models.ForeignKey(Funcionarios, models.DO_NOTHING, db_column='COD_CONF')  # Field name made lowercase.
    data_conf = models.DateTimeField(db_column='DATA_CONF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DETFINAL_CONF'
        unique_together = (('cod_os', 'cod_conf'),)


class ItmOsDetfinalSepara(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_separa = models.BigIntegerField(db_column='COD_SEPARA', blank=True, null=True)  # Field name made lowercase.
    data_separa = models.DateTimeField(db_column='DATA_SEPARA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DETFINAL_SEPARA'


class ItmOsDetlib(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS')  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='Cod_Prod')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='Qtde', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DETLIB'
        unique_together = (('cod_os', 'data', 'cod_prod'),)


class ItmOsDetpagto(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS')  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='Cod_Pagto', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data')  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor', blank=True, null=True)  # Field name made lowercase.
    num_che = models.CharField(db_column='Num_Che', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_ban = models.BigIntegerField(db_column='Cod_Ban', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DETPAGTO'
        unique_together = (('cod_os', 'data'),)


class ItmOsDetAndamento(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', primary_key=True)  # Field name made lowercase.
    qtde_os = models.IntegerField(db_column='Qtde_OS', blank=True, null=True)  # Field name made lowercase.
    desc_os = models.CharField(db_column='Desc_OS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    det_status_os = models.CharField(db_column='Det_Status_OS', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_DET_ANDAMENTO'


class ItmOsEmba(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    cod_caixa = models.ForeignKey(EmbalagemTechcd, models.DO_NOTHING, db_column='COD_CAIXA')  # Field name made lowercase.
    qtde_caixa = models.IntegerField(db_column='QTDE_CAIXA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_EMBA'
        unique_together = (('cod_os', 'cod_caixa'),)


class ItmOsImportado(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde = models.BigIntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_IMPORTADO'


class ItmOsMemorando(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', primary_key=True)  # Field name made lowercase.
    mem_os = models.TextField(db_column='MEM_OS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_MEMORANDO'


class ItmOsPagto(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    parcnum_os = models.BigIntegerField(db_column='PARCNUM_OS')  # Field name made lowercase.
    cod_pagto = models.ForeignKey('TipoPagto', models.DO_NOTHING, db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.ForeignKey(FormaPagto, models.DO_NOTHING, db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    val_pagto = models.DecimalField(db_column='VAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datavenc_pagto = models.DateTimeField(db_column='DATAVENC_PAGTO', blank=True, null=True)  # Field name made lowercase.
    taxa_os = models.FloatField(db_column='TAXA_OS', blank=True, null=True)  # Field name made lowercase.
    quit_os = models.NullBooleanField(db_column='QUIT_OS')  # Field name made lowercase.
    quemquit_os = models.CharField(db_column='QUEMQUIT_OS', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dataquit_os = models.DateTimeField(db_column='DATAQUIT_OS', blank=True, null=True)  # Field name made lowercase.
    cod2_pagto = models.BigIntegerField(db_column='COD2_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod2_frmpagto = models.BigIntegerField(db_column='COD2_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    chq_pagto = models.CharField(db_column='CHQ_PAGTO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    capt_pagto = models.NullBooleanField(db_column='CAPT_PAGTO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_PAGTO'
        unique_together = (('cod_os', 'parcnum_os'),)


class ItmOsPagtoParc(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    parcnum_os = models.BigIntegerField(db_column='PARCNUM_OS', blank=True, null=True)  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quemquit_os = models.CharField(db_column='QUEMQUIT_OS', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_PAGTO_PARC'


class ItmOsRejeit(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_rejeit = models.BigIntegerField(db_column='QTDE_REJEIT')  # Field name made lowercase.
    data_rejeit = models.DateTimeField(db_column='DATA_REJEIT')  # Field name made lowercase.
    cod_solicitante = models.IntegerField(db_column='COD_SOLICITANTE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_REJEIT'


class ItmOsRem(models.Model):
    cod_os = models.ForeignKey(ItmOs, models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    cod_prod = models.ForeignKey(ItmOs, models.DO_NOTHING, db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.ForeignKey(ItmOs, models.DO_NOTHING, db_column='COD_SERV')  # Field name made lowercase.
    qtde_rem = models.FloatField(db_column='QTDE_REM', blank=True, null=True)  # Field name made lowercase.
    empresa_rem = models.CharField(db_column='EMPRESA_REM', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_OS_REM'


class ItmProdexp(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde = models.BigIntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_PRODEXP'


class ItmRequis(models.Model):
    cod_requis = models.ForeignKey('RequisMaterial', models.DO_NOTHING, db_column='COD_REQUIS')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    qtde_requis = models.IntegerField(db_column='QTDE_REQUIS', blank=True, null=True)  # Field name made lowercase.
    said_requis = models.IntegerField(db_column='SAID_REQUIS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_REQUIS'
        unique_together = (('cod_requis', 'cod_prod'),)


class ItmRequisDel(models.Model):
    cod_requis_del = models.BigIntegerField(db_column='COD_REQUIS_DEL', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde_requis_del = models.IntegerField(db_column='QTDE_REQUIS_DEL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_REQUIS_DEL'


class ItmReserv(models.Model):
    cod_reserv = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='COD_RESERV')  # Field name made lowercase.
    cod_prod = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='COD_PROD')  # Field name made lowercase.
    qtde_reserv = models.IntegerField(db_column='QTDE_RESERV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_RESERV'
        unique_together = (('cod_reserv', 'cod_prod'),)


class ItmSolprazoServ(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    tipo_itm = models.BigIntegerField(db_column='TIPO_ITM', blank=True, null=True)  # Field name made lowercase.
    desc_itm = models.CharField(db_column='DESC_ITM', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_SOLPRAZO_SERV'


class ItmSolNfsilk(models.Model):
    cod_requis = models.BigIntegerField(db_column='Cod_Requis')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='Cod_Prod')  # Field name made lowercase.
    qtde_sol = models.IntegerField(db_column='Qtde_Sol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_SOL_NFSILK'
        unique_together = (('cod_requis', 'cod_prod'),)


class ItmSolNfInterna(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    qtde_sol = models.BigIntegerField(db_column='QTDE_SOL')  # Field name made lowercase.
    qtde_ativo = models.BigIntegerField(db_column='QTDE_ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_SOL_NF_INTERNA'


class ItmSolNfRemessa(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde_sol = models.BigIntegerField(db_column='QTDE_SOL', blank=True, null=True)  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_SOL_NF_REMESSA'


class ItmSolNfSaida(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL')  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='COD_OS')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_sol = models.IntegerField(db_column='QTDE_SOL', blank=True, null=True)  # Field name made lowercase.
    qtdenf_sol = models.IntegerField(db_column='QTDENF_SOL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_SOL_NF_SAIDA'


class ItmSolRemessaPagto(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    parcnum_sol = models.IntegerField(db_column='PARCNUM_SOL', blank=True, null=True)  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.BigIntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    valor_sol = models.DecimalField(db_column='VALOR_SOL', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_SOL_REMESSA_PAGTO'


class ItmTipoEnvioEmail(models.Model):
    cod_tip = models.BigIntegerField(blank=True, null=True)
    cod_func = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ITM_TIPO_ENVIO_EMAIL'


class ItmTipoEnvioTorpedo(models.Model):
    cod_tip = models.BigIntegerField(db_column='COD_TIP', blank=True, null=True)  # Field name made lowercase.
    apelido_user = models.CharField(db_column='APELIDO_USER', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITM_TIPO_ENVIO_TORPEDO'


class Iva(models.Model):
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    iva = models.FloatField(db_column='IVA', blank=True, null=True)  # Field name made lowercase.
    aliq_interna = models.FloatField(db_column='Aliq_Interna', blank=True, null=True)  # Field name made lowercase.
    aliq_interestadual = models.FloatField(db_column='Aliq_Interestadual', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IVA'


class ImpressaoOs(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    imprimiu = models.CharField(db_column='Imprimiu', max_length=3, blank=True, null=True)  # Field name made lowercase.
    data_imp = models.DateTimeField(db_column='Data_Imp', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Impressao_OS'


class ItmRma(models.Model):
    cod_rma = models.BigIntegerField(db_column='COD_RMA', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde_os = models.BigIntegerField(db_column='QTDE_OS', blank=True, null=True)  # Field name made lowercase.
    qtde_rma = models.BigIntegerField(db_column='QTDE_RMA', blank=True, null=True)  # Field name made lowercase.
    descdef_rma = models.TextField(db_column='DESCDEF_RMA', blank=True, null=True)  # Field name made lowercase.
    aceito_rma = models.NullBooleanField(db_column='ACEITO_RMA')  # Field name made lowercase.
    obsaceito_rma = models.TextField(db_column='OBSACEITO_RMA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Itm_RMA'


class LcTeste(models.Model):
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LC_TESTE'


class ListaEmails(models.Model):
    emails = models.CharField(db_column='EMAILS', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_EMAILS'


class LocalidadeCep(models.Model):
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cep = models.BigIntegerField(db_column='Cep', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localidade = models.CharField(db_column='Localidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCALIDADE_CEP'


class LocalidadeCidades(models.Model):
    cep = models.BigIntegerField(db_column='Cep', blank=True, null=True)  # Field name made lowercase.
    localidade = models.CharField(db_column='Localidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCALIDADE_CIDADES'


class LocalidadeEncNormal(models.Model):
    unidade_fed = models.CharField(db_column='UNIDADE_FED', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sigla_local = models.CharField(db_column='SIGLA_LOCAL', primary_key=True, max_length=2)  # Field name made lowercase.
    capital = models.CharField(db_column='CAPITAL', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCALIDADE_ENC_NORMAL'


class LocalidadeFaixabairros(models.Model):
    bairro = models.CharField(db_column='Bairro', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cepinicial = models.BigIntegerField(db_column='CepInicial', blank=True, null=True)  # Field name made lowercase.
    cepfinal = models.BigIntegerField(db_column='CepFinal', blank=True, null=True)  # Field name made lowercase.
    localidade = models.CharField(db_column='Localidade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCALIDADE_FAIXABAIRROS'


class LogCredito(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    data_cre = models.DateTimeField(db_column='DATA_CRE')  # Field name made lowercase.
    cod_cre = models.ForeignKey(CliCredito, models.DO_NOTHING, db_column='COD_CRE')  # Field name made lowercase.
    nome_cre = models.CharField(db_column='NOME_CRE', max_length=50)  # Field name made lowercase.
    valid_cre = models.DateTimeField(db_column='VALID_CRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_CREDITO'
        unique_together = (('cod_cli', 'data_cre'),)


class LogImpressaoOsProd(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS')  # Field name made lowercase.
    data_imp = models.DateTimeField(db_column='Data_Imp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_IMPRESSAO_OS_PROD'
        unique_together = (('cod_os', 'data_imp'),)


class LogPerfilAlteracoes(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    operacao = models.CharField(db_column='OPERACAO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_PERFIL_ALTERACOES'


class LogPrecos(models.Model):
    cod_logp = models.BigIntegerField(db_column='COD_LOGP', primary_key=True)  # Field name made lowercase.
    cod_func = models.BigIntegerField(db_column='COD_FUNC')  # Field name made lowercase.
    data_logp = models.DateTimeField(db_column='DATA_LOGP')  # Field name made lowercase.
    cod_ref = models.BigIntegerField(db_column='COD_REF')  # Field name made lowercase.
    tipo_ref = models.CharField(db_column='TIPO_REF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV', blank=True, null=True)  # Field name made lowercase.
    valortab_logp = models.DecimalField(db_column='VALORTAB_LOGP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valormod_logp = models.DecimalField(db_column='VALORMOD_LOGP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_PRECOS'


class LogRemessaTotal(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    user_log = models.CharField(db_column='USER_LOG', max_length=20, blank=True, null=True)  # Field name made lowercase.
    data_log = models.DateTimeField(db_column='DATA_LOG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_REMESSA_TOTAL'


class LogReservas(models.Model):
    cod_logr = models.BigIntegerField(db_column='COD_LOGR', primary_key=True)  # Field name made lowercase.
    data_logr = models.DateTimeField(db_column='DATA_LOGR')  # Field name made lowercase.
    cod_func = models.BigIntegerField(db_column='COD_FUNC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_RESERVAS'


class LogSaldoProd(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    tela = models.CharField(db_column='TELA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    saldo_fisico = models.BigIntegerField(db_column='SALDO_FISICO', blank=True, null=True)  # Field name made lowercase.
    saldo_teorico = models.BigIntegerField(db_column='SALDO_TEORICO', blank=True, null=True)  # Field name made lowercase.
    requisitada = models.BigIntegerField(db_column='REQUISITADA', blank=True, null=True)  # Field name made lowercase.
    reservada = models.BigIntegerField(db_column='RESERVADA', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    validacao = models.BigIntegerField(db_column='VALIDACAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_SALDO_PROD'


class LogSenhaAdmin(models.Model):
    data_log = models.DateTimeField(db_column='Data_Log')  # Field name made lowercase.
    usu_log = models.CharField(db_column='Usu_Log', max_length=50)  # Field name made lowercase.
    desc_log = models.CharField(db_column='Desc_Log', max_length=300)  # Field name made lowercase.
    cod_oper = models.BigIntegerField(db_column='Cod_Oper')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_SENHA_ADMIN'


class Loja(models.Model):
    cod_os = models.ForeignKey('Os', models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    cod_loja = models.BigIntegerField(db_column='COD_LOJA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOJA'
        unique_together = (('cod_os', 'cod_loja'),)


class LojaItmPedidos(models.Model):
    idpedido = models.IntegerField(blank=True, null=True)
    idproduto = models.IntegerField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOJA_ITM_PEDIDOS'


class LojaOrcamentos(models.Model):
    cod_loja = models.BigIntegerField(db_column='COD_LOJA', blank=True, null=True)  # Field name made lowercase.
    cod_orca = models.BigIntegerField(db_column='COD_ORCA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOJA_ORCAMENTOS'


class LojaPedidos(models.Model):
    idpedido = models.BigIntegerField()
    data1_os = models.DateTimeField(db_column='DATA1_OS', blank=True, null=True)  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT')  # Field name made lowercase.
    tot_os = models.DecimalField(db_column='TOT_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_os = models.DecimalField(db_column='FRETE_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesoprod_os = models.FloatField(db_column='PESOPROD_OS', blank=True, null=True)  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_os = models.DecimalField(db_column='DESCSUFRAMA_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    nome_trans_ent = models.CharField(db_column='NOME_TRANS_ENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddd_trans_ent = models.CharField(db_column='DDD_TRANS_ENT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    telefone_trans_ent = models.CharField(db_column='TELEFONE_TRANS_ENT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pagcomp1 = models.CharField(max_length=2550, blank=True, null=True)
    email_cli = models.CharField(db_column='EMAIL_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contato_cli = models.CharField(db_column='CONTATO_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg_cli = models.CharField(db_column='RG_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd2_cli = models.CharField(db_column='DDD2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_cli = models.CharField(db_column='TEL2_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    suframa_cli = models.CharField(db_column='SUFRAMA_CLI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    revenda_cli = models.CharField(db_column='REVENDA_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_divulg = models.BigIntegerField(db_column='COD_DIVULG', blank=True, null=True)  # Field name made lowercase.
    export = models.NullBooleanField()
    num_cartao = models.CharField(max_length=16, blank=True, null=True)
    cod_seguranca = models.CharField(max_length=3, blank=True, null=True)
    cod_legivel = models.NullBooleanField()
    data_validade = models.DateTimeField(blank=True, null=True)
    nome_impresso = models.CharField(max_length=50, blank=True, null=True)
    sobrenome_cli = models.CharField(db_column='SOBRENOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOJA_PEDIDOS'


class Manutencao(models.Model):
    cod_solicitacao = models.BigAutoField(primary_key=True)
    nome_solicitante = models.CharField(max_length=30, blank=True, null=True)
    data_solicitacao = models.DateTimeField(blank=True, null=True)
    data_atendimento = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=2, blank=True, null=True)
    det_solicitacao = models.CharField(max_length=1000, blank=True, null=True)
    tipo_solicitacao = models.CharField(max_length=2, blank=True, null=True)
    prioridade = models.CharField(max_length=1, blank=True, null=True)
    det_atendimento = models.CharField(max_length=1000, blank=True, null=True)
    status_user = models.CharField(max_length=2, blank=True, null=True)
    nome_atend = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MANUTENCAO'


class MensagensProd(models.Model):
    cod_solicitacao = models.ForeignKey('SolicitacaoProd', models.DO_NOTHING, db_column='Cod_Solicitacao', blank=True, null=True)  # Field name made lowercase.
    desc_mensagem = models.CharField(db_column='Desc_Mensagem', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='Cod_Prod', blank=True, null=True)  # Field name made lowercase.
    tipo_solicitacao = models.CharField(db_column='Tipo_Solicitacao', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MENSAGENS_PROD'


class Mercados(models.Model):
    cod_mercado = models.DecimalField(primary_key=True, max_digits=18, decimal_places=0)
    desc_mercado = models.CharField(max_length=30, blank=True, null=True)
    total_prospects = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    data_inclusao = models.DateTimeField(blank=True, null=True)
    estima_orcamentos = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    estima_clientes = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    assunto_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MERCADOS'


class ModeloNf(models.Model):
    cod_mod = models.BigIntegerField(db_column='Cod_Mod')  # Field name made lowercase.
    desc_mod = models.CharField(db_column='Desc_Mod', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODELO_NF'


class ModeloNfeEntrada(models.Model):
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    desc_mod = models.CharField(db_column='DESC_MOD', max_length=80, blank=True, null=True)  # Field name made lowercase.
    data_mod = models.DateTimeField(db_column='Data_MOD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODELO_NFE_ENTRADA'


class Motivos(models.Model):
    cod_mot_orca = models.DecimalField(db_column='Cod_Mot_Orca', primary_key=True, max_digits=18, decimal_places=0)  # Field name made lowercase.
    desc_mot_orca = models.CharField(db_column='Desc_Mot_Orca', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc_infoadi_mot_orca = models.CharField(db_column='Desc_InfoAdi_Mot_Orca', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOTIVOS'


class MotivosCanc(models.Model):
    cod_motcanc = models.BigIntegerField(db_column='Cod_MotCanc', primary_key=True)  # Field name made lowercase.
    desc_motcanc = models.CharField(db_column='Desc_MotCanc', max_length=70, blank=True, null=True)  # Field name made lowercase.
    lib_cliente = models.NullBooleanField(db_column='Lib_Cliente')  # Field name made lowercase.
    lib_contato = models.NullBooleanField(db_column='Lib_Contato')  # Field name made lowercase.
    lib_vendedor = models.NullBooleanField(db_column='Lib_Vendedor')  # Field name made lowercase.
    lib_datapedido = models.NullBooleanField(db_column='Lib_DataPedido')  # Field name made lowercase.
    lib_tabela = models.NullBooleanField(db_column='Lib_Tabela')  # Field name made lowercase.
    lib_tipopagto = models.NullBooleanField(db_column='Lib_TipoPagto')  # Field name made lowercase.
    lib_formapagto = models.NullBooleanField(db_column='Lib_FormaPagto')  # Field name made lowercase.
    lib_entrega = models.NullBooleanField(db_column='Lib_Entrega')  # Field name made lowercase.
    lib_bv = models.NullBooleanField(db_column='Lib_BV')  # Field name made lowercase.
    lib_dataentrega = models.NullBooleanField(db_column='Lib_DataEntrega')  # Field name made lowercase.
    lib_produtos = models.NullBooleanField(db_column='Lib_Produtos')  # Field name made lowercase.
    lib_servicos = models.NullBooleanField(db_column='Lib_Servicos')  # Field name made lowercase.
    lib_freteconta = models.NullBooleanField(db_column='Lib_FreteConta')  # Field name made lowercase.
    lib_haamostra = models.NullBooleanField(db_column='Lib_haAmostra')  # Field name made lowercase.
    lib_observacao = models.NullBooleanField(db_column='Lib_Observacao')  # Field name made lowercase.
    lib_produtoqtde = models.NullBooleanField(db_column='Lib_ProdutoQTDE')  # Field name made lowercase.
    lib_produtovalor = models.NullBooleanField(db_column='Lib_ProdutoVALOR')  # Field name made lowercase.
    lib_servicoqtde = models.NullBooleanField(db_column='Lib_ServicoQTDE')  # Field name made lowercase.
    lib_servicovalor = models.NullBooleanField(db_column='Lib_ServicoVALOR')  # Field name made lowercase.
    canc_definitivo = models.NullBooleanField(db_column='Canc_Definitivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOTIVOS_CANC'


class MotivosOrcamentoPerdido(models.Model):
    cod_orca = models.DecimalField(db_column='COD_ORCA', max_digits=18, decimal_places=0)  # Field name made lowercase.
    cod_cli = models.DecimalField(db_column='COD_CLI', max_digits=18, decimal_places=0)  # Field name made lowercase.
    cod_mot_orca = models.DecimalField(db_column='COD_MOT_ORCA', max_digits=18, decimal_places=0)  # Field name made lowercase.
    obs_mot_orca = models.CharField(db_column='OBS_MOT_ORCA', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOTIVOS_ORCAMENTO_PERDIDO'
        unique_together = (('cod_orca', 'cod_cli', 'cod_mot_orca'),)


class MotoBoy(models.Model):
    opcao_mboy = models.IntegerField(db_column='OPCAO_MBOY')  # Field name made lowercase.
    frete_mboy = models.DecimalField(db_column='FRETE_MBOY', max_digits=19, decimal_places=4)  # Field name made lowercase.
    frete_pri = models.DecimalField(db_column='FRETE_PRI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_urg = models.DecimalField(db_column='FRETE_URG', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_tar = models.DecimalField(db_column='FRETE_TAR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOTO_BOY'


class Movimentacao(models.Model):
    cod_prod = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldoacum_mov = models.FloatField(db_column='SALDOACUM_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIMENTACAO'


class MovimentacaoData(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=2)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=80, blank=True, null=True)  # Field name made lowercase.
    saldoacum_mov = models.FloatField(db_column='SALDOACUM_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=40)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=40)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=40)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIMENTACAO_DATA'


class MovimentacaoDatastore(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldodata_mov = models.BigIntegerField(db_column='SALDODATA_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldototal_mov = models.BigIntegerField(db_column='SALDOTOTAL_MOV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIMENTACAO_DATASTORE'


class MovimentacaoMidia(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=2)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=80, blank=True, null=True)  # Field name made lowercase.
    saldoacum_mov = models.FloatField(db_column='SALDOACUM_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=40)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=40)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=40)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIMENTACAO_MIDIA'


class MovimentacaoMidiacenter(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldomidia_mov = models.BigIntegerField(db_column='SALDOMIDIA_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldototal_mov = models.BigIntegerField(db_column='SALDOTOTAL_MOV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIMENTACAO_MIDIACENTER'


class MovimentacaoTechcd(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldotech_mov = models.BigIntegerField(db_column='SALDOTECH_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldototal_mov = models.BigIntegerField(db_column='SALDOTOTAL_MOV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVIMENTACAO_TECHCD'


class MovIcms(models.Model):
    cod_ref = models.BigIntegerField(db_column='COD_REF')  # Field name made lowercase.
    data_mov_icms = models.DateTimeField(db_column='DATA_MOV_ICMS')  # Field name made lowercase.
    tipo_mov_icms = models.CharField(db_column='TIPO_MOV_ICMS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valor_mov_icms = models.DecimalField(db_column='VALOR_MOV_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    empresa_mov_icms = models.CharField(db_column='EMPRESA_MOV_ICMS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOV_ICMS'
        unique_together = (('cod_ref', 'data_mov_icms'),)


class Municipios(models.Model):
    uf = models.CharField(db_column='UF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_municip = models.BigIntegerField(db_column='Cod_municip', blank=True, null=True)  # Field name made lowercase.
    nome_municip = models.CharField(db_column='Nome_municip', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MUNICIPIOS'


class Mva(models.Model):
    ncm = models.CharField(db_column='NCM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc_tipi = models.CharField(db_column='DESC_TIPI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    desc_st_sp = models.CharField(db_column='DESC_ST_SP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    porcentagem_iva = models.FloatField(db_column='PORCENTAGEM_IVA', blank=True, null=True)  # Field name made lowercase.
    status = models.FloatField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MVA'


class MvaImportados(models.Model):
    cf_uf = models.CharField(db_column='CF_UF', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ac = models.CharField(db_column='AC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    al = models.CharField(db_column='AL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ap = models.CharField(db_column='AP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    am = models.CharField(db_column='AM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ba = models.CharField(db_column='BA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ce = models.CharField(db_column='CE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    df = models.CharField(db_column='DF', max_length=12, blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=12, blank=True, null=True)  # Field name made lowercase.
    go = models.CharField(db_column='GO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ma = models.CharField(db_column='MA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mt = models.CharField(db_column='MT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ms = models.CharField(db_column='MS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mg = models.CharField(db_column='MG', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pb = models.CharField(db_column='PB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pr = models.CharField(db_column='PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pe = models.CharField(db_column='PE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pi = models.CharField(db_column='PI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rj = models.CharField(db_column='RJ', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rn = models.CharField(db_column='RN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ro = models.CharField(db_column='RO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rr = models.CharField(db_column='RR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sc = models.CharField(db_column='SC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sp = models.CharField(db_column='SP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    se = models.CharField(db_column='SE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    to = models.CharField(db_column='TO', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MVA_IMPORTADOS'


class MvaNacionais(models.Model):
    cf_uf = models.CharField(db_column='CF_UF', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ac = models.CharField(db_column='AC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    al = models.CharField(db_column='AL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ap = models.CharField(db_column='AP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    am = models.CharField(db_column='AM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ba = models.CharField(db_column='BA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ce = models.CharField(db_column='CE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    df = models.CharField(db_column='DF', max_length=12, blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=12, blank=True, null=True)  # Field name made lowercase.
    go = models.CharField(db_column='GO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ma = models.CharField(db_column='MA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mt = models.CharField(db_column='MT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ms = models.CharField(db_column='MS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mg = models.CharField(db_column='MG', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pb = models.CharField(db_column='PB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pr = models.CharField(db_column='PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pe = models.CharField(db_column='PE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pi = models.CharField(db_column='PI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rj = models.CharField(db_column='RJ', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rn = models.CharField(db_column='RN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ro = models.CharField(db_column='RO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rr = models.CharField(db_column='RR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sc = models.CharField(db_column='SC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sp = models.CharField(db_column='SP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    se = models.CharField(db_column='SE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    to = models.CharField(db_column='TO', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MVA_NACIONAIS'


class MvaOrig(models.Model):
    cf_uf = models.CharField(db_column='CF_UF', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ac = models.CharField(db_column='AC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    al = models.CharField(db_column='AL', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ap = models.CharField(db_column='AP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    am = models.CharField(db_column='AM', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ba = models.CharField(db_column='BA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ce = models.CharField(db_column='CE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    df = models.CharField(db_column='DF', max_length=12, blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=12, blank=True, null=True)  # Field name made lowercase.
    go = models.CharField(db_column='GO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ma = models.CharField(db_column='MA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mt = models.CharField(db_column='MT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ms = models.CharField(db_column='MS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    mg = models.CharField(db_column='MG', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pa = models.CharField(db_column='PA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pb = models.CharField(db_column='PB', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pr = models.CharField(db_column='PR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pe = models.CharField(db_column='PE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    pi = models.CharField(db_column='PI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rj = models.CharField(db_column='RJ', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rn = models.CharField(db_column='RN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rs = models.CharField(db_column='RS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ro = models.CharField(db_column='RO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rr = models.CharField(db_column='RR', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sc = models.CharField(db_column='SC', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sp = models.CharField(db_column='SP', max_length=12, blank=True, null=True)  # Field name made lowercase.
    se = models.CharField(db_column='SE', max_length=12, blank=True, null=True)  # Field name made lowercase.
    to = models.CharField(db_column='TO', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MVA_ORIG'


class MvaSt(models.Model):
    ncm = models.CharField(db_column='NCM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc_tipi = models.TextField(db_column='DESC_TIPI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc_st_sp = models.TextField(db_column='DESC_ST_SP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    porcentagem_iva = models.CharField(db_column='PORCENTAGEM_IVA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dt_cadastro = models.DateTimeField(db_column='DT_CADASTRO', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MVA_ST'


class NaturezaEnt(models.Model):
    cod_nat = models.CharField(db_column='Cod_Nat', max_length=5)  # Field name made lowercase.
    desc_nat = models.CharField(db_column='Desc_Nat', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATUREZA_ENT'


class NaturezaOperacao(models.Model):
    cod_nat = models.IntegerField(db_column='COD_NAT')  # Field name made lowercase.
    desc_nat = models.CharField(db_column='DESC_NAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cfop_nat = models.CharField(db_column='CFOP_NAT', max_length=18, blank=True, null=True)  # Field name made lowercase.
    inter_nat = models.IntegerField(db_column='INTER_NAT', blank=True, null=True)  # Field name made lowercase.
    icms_nat = models.IntegerField(db_column='ICMS_NAT', blank=True, null=True)  # Field name made lowercase.
    tipo_nf = models.CharField(db_column='TIPO_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sittribut_nat = models.CharField(db_column='SITTRIBUT_NAT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    direcao_nat = models.CharField(db_column='DIRECAO_NAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    base_legal = models.CharField(db_column='BASE_LEGAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    outras_icms = models.NullBooleanField(db_column='OUTRAS_ICMS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATUREZA_OPERACAO'


class NaturezaOperacaoBkp(models.Model):
    cod_nat = models.IntegerField(db_column='COD_NAT', primary_key=True)  # Field name made lowercase.
    desc_nat = models.CharField(db_column='DESC_NAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cfop_nat = models.CharField(db_column='CFOP_NAT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inter_nat = models.IntegerField(db_column='INTER_NAT', blank=True, null=True)  # Field name made lowercase.
    icms_nat = models.IntegerField(db_column='ICMS_NAT', blank=True, null=True)  # Field name made lowercase.
    tipo_nf = models.CharField(db_column='TIPO_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sittribut_nat = models.CharField(db_column='SITTRIBUT_NAT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    direcao_nat = models.CharField(db_column='DIRECAO_NAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    base_legal = models.CharField(db_column='BASE_LEGAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    outras_icms = models.NullBooleanField(db_column='OUTRAS_ICMS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NATUREZA_OPERACAO_BKP'


class Ncm(models.Model):
    ncm = models.CharField(db_column='NCM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='Descricao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NCM'


class Nfe(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFE'


class NfeData(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA')  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFE_DATA'


class NfeDataSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA')  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFE_DATA_SRV'


class NfeMidia(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFE_MIDIA'


class NfeMidiaSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFE_MIDIA_SRV'


class NfeSrv(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFE_SRV'


class NfDevolCli(models.Model):
    cod_devol_cli = models.BigIntegerField(db_column='COD_DEVOL_CLI', primary_key=True)  # Field name made lowercase.
    cod_nf_saida = models.ForeignKey('NotasFiscais', models.DO_NOTHING, db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.ForeignKey(NaturezaOperacaoBkp, models.DO_NOTHING, db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    totgeral_devol_cli = models.DecimalField(db_column='TOTGERAL_DEVOL_CLI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    datanf_devol_cli = models.DateTimeField(db_column='DATANF_DEVOL_CLI', blank=True, null=True)  # Field name made lowercase.
    motivnf_devol_cli = models.TextField(db_column='MOTIVNF_DEVOL_CLI', blank=True, null=True)  # Field name made lowercase.
    obs_devol_cli = models.DecimalField(db_column='OBS_DEVOL_CLI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NF_DEVOL_CLI'


class NfDevolForn(models.Model):
    cod_devol_forn = models.BigIntegerField(db_column='COD_DEVOL_FORN', primary_key=True)  # Field name made lowercase.
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.ForeignKey(Fornecedores, models.DO_NOTHING, db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.BigIntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    dataemis_devol_forn = models.DateTimeField(db_column='DATAEMIS_DEVOL_FORN', blank=True, null=True)  # Field name made lowercase.
    datasaid_devol_forn = models.DateTimeField(db_column='DATASAID_DEVOL_FORN', blank=True, null=True)  # Field name made lowercase.
    valtotal_devol_forn = models.DecimalField(db_column='VALTOTAL_DEVOL_FORN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motivnf_devol_forn = models.TextField(db_column='MOTIVNF_DEVOL_FORN', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NF_DEVOL_FORN'


class NfSaidaComentrada(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    possui_nf_entrada = models.NullBooleanField(db_column='POSSUI_NF_ENTRADA')  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NF_SAIDA_COMENTRADA'


class NfeCanc(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    quemcanc_nf_saida = models.CharField(db_column='QUEMCANC_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    motivcanc_nf_saida = models.TextField(db_column='MOTIVCANC_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    datacanc_nf_saida = models.DateTimeField(db_column='DATACANC_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFe_CANC'


class Niveis(models.Model):
    cod_niv = models.BigIntegerField(db_column='COD_NIV', primary_key=True)  # Field name made lowercase.
    desc_niv = models.CharField(db_column='DESC_NIV', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NIVEIS'


class NiveisOper(models.Model):
    cod_niv = models.ForeignKey(Niveis, models.DO_NOTHING, db_column='COD_NIV')  # Field name made lowercase.
    cod_oper = models.ForeignKey('Operacoes', models.DO_NOTHING, db_column='COD_OPER')  # Field name made lowercase.
    inc_oper = models.BooleanField(db_column='INC_OPER')  # Field name made lowercase.
    exc_oper = models.BooleanField(db_column='EXC_OPER')  # Field name made lowercase.
    alt_oper = models.BooleanField(db_column='ALT_OPER')  # Field name made lowercase.
    cons_oper = models.BooleanField(db_column='CONS_OPER')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NIVEIS_OPER'
        unique_together = (('cod_niv', 'cod_oper'),)


class Nop(models.Model):
    cod_nat = models.IntegerField(db_column='COD_NAT')  # Field name made lowercase.
    desc_nat = models.CharField(db_column='DESC_NAT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cfop_nat = models.CharField(db_column='CFOP_NAT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inter_nat = models.IntegerField(db_column='INTER_NAT', blank=True, null=True)  # Field name made lowercase.
    icms_nat = models.IntegerField(db_column='ICMS_NAT', blank=True, null=True)  # Field name made lowercase.
    tipo_nf = models.CharField(db_column='TIPO_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sittribut_nat = models.CharField(db_column='SITTRIBUT_NAT', max_length=3, blank=True, null=True)  # Field name made lowercase.
    direcao_nat = models.CharField(db_column='DIRECAO_NAT', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOP'


class NotasFiscais(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', primary_key=True)  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS'


class NotasFiscaisCanc(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    quemcanc_nf_saida = models.CharField(db_column='QUEMCANC_NF_SAIDA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    motivcanc_nf_saida = models.TextField(db_column='MOTIVCANC_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    datacanc_nf_saida = models.DateTimeField(db_column='DATACANC_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_CANC'


class NotasFiscaisData(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=2)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=2)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA')  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=100)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=28)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=36)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=38)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=100)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=40)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=40)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=60)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=4)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=18)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=4)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=18)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=20)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_DATA'


class NotasFiscaisDev(models.Model):
    cod_nf_dev = models.BigIntegerField(db_column='COD_NF_DEV', blank=True, null=True)  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_DEV'


class NotasFiscaisEntrada(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA', primary_key=True)  # Field name made lowercase.
    numdoc_nf_entrada = models.CharField(db_column='NUMDOC_NF_ENTRADA', max_length=20)  # Field name made lowercase.
    valtotal_nf_entrada = models.DecimalField(db_column='VALTOTAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valicms_nf_entrada = models.DecimalField(db_column='VALICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valipi_nf_entrada = models.DecimalField(db_column='VALIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valiss_nf_entrada = models.DecimalField(db_column='VALISS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valenvio_nf_entrada = models.DecimalField(db_column='VALENVIO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.ForeignKey(Fornecedores, models.DO_NOTHING, db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    data_emiss = models.DateTimeField(db_column='DATA_EMISS', blank=True, null=True)  # Field name made lowercase.
    nome_nf_entrada = models.CharField(db_column='NOME_NF_ENTRADA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnpj_nf_entrada = models.CharField(db_column='CNPJ_NF_ENTRADA', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_nf_entrada = models.CharField(db_column='IE_NF_ENTRADA', max_length=19, blank=True, null=True)  # Field name made lowercase.
    uf_nf_entrada = models.CharField(db_column='UF_NF_ENTRADA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    modelo_nf_entrada = models.IntegerField(db_column='MODELO_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    serie_nf_entrada = models.IntegerField(db_column='SERIE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_ENTRADA'


class NotasFiscaisEntradaData(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    numdoc_nf_entrada = models.CharField(db_column='NUMDOC_NF_ENTRADA', max_length=20)  # Field name made lowercase.
    valtotal_nf_entrada = models.DecimalField(db_column='VALTOTAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valicms_nf_entrada = models.DecimalField(db_column='VALICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valipi_nf_entrada = models.DecimalField(db_column='VALIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valiss_nf_entrada = models.DecimalField(db_column='VALISS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valenvio_nf_entrada = models.DecimalField(db_column='VALENVIO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.BigIntegerField(db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    data_emiss = models.DateTimeField(db_column='DATA_EMISS', blank=True, null=True)  # Field name made lowercase.
    nome_nf_entrada = models.CharField(db_column='NOME_NF_ENTRADA', max_length=50)  # Field name made lowercase.
    cnpj_nf_entrada = models.CharField(db_column='CNPJ_NF_ENTRADA', max_length=18)  # Field name made lowercase.
    ie_nf_entrada = models.CharField(db_column='IE_NF_ENTRADA', max_length=19)  # Field name made lowercase.
    uf_nf_entrada = models.CharField(db_column='UF_NF_ENTRADA', max_length=2)  # Field name made lowercase.
    modelo_nf_entrada = models.IntegerField(db_column='MODELO_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    serie_nf_entrada = models.IntegerField(db_column='SERIE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_ENTRADA_DATA'


class NotasFiscaisEntradaMidia(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    numdoc_nf_entrada = models.CharField(db_column='NUMDOC_NF_ENTRADA', max_length=20)  # Field name made lowercase.
    valtotal_nf_entrada = models.DecimalField(db_column='VALTOTAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valicms_nf_entrada = models.DecimalField(db_column='VALICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valipi_nf_entrada = models.DecimalField(db_column='VALIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valiss_nf_entrada = models.DecimalField(db_column='VALISS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valenvio_nf_entrada = models.DecimalField(db_column='VALENVIO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.BigIntegerField(db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    data_emiss = models.DateTimeField(db_column='DATA_EMISS', blank=True, null=True)  # Field name made lowercase.
    nome_nf_entrada = models.CharField(db_column='NOME_NF_ENTRADA', max_length=50)  # Field name made lowercase.
    cnpj_nf_entrada = models.CharField(db_column='CNPJ_NF_ENTRADA', max_length=18)  # Field name made lowercase.
    ie_nf_entrada = models.CharField(db_column='IE_NF_ENTRADA', max_length=19)  # Field name made lowercase.
    uf_nf_entrada = models.CharField(db_column='UF_NF_ENTRADA', max_length=2)  # Field name made lowercase.
    modelo_nf_entrada = models.IntegerField(db_column='MODELO_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    serie_nf_entrada = models.IntegerField(db_column='SERIE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_ENTRADA_MIDIA'


class NotasFiscaisMidia(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    tipo_nf_saida = models.CharField(db_column='TIPO_NF_SAIDA', max_length=2)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    imprimefrete_nf_saida = models.NullBooleanField(db_column='IMPRIMEFRETE_NF_SAIDA')  # Field name made lowercase.
    pagafrete_nf_saida = models.CharField(db_column='PAGAFRETE_NF_SAIDA', max_length=2)  # Field name made lowercase.
    dataemis_nf_saida = models.DateTimeField(db_column='DATAEMIS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.IntegerField(db_column='COD_NAT', blank=True, null=True)  # Field name made lowercase.
    valicms_nf_saida = models.IntegerField(db_column='VALICMS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    valiss_nf_saida = models.IntegerField(db_column='VALISS_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    totprod_nf_saida = models.DecimalField(db_column='TOTPROD_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totserv_nf_saida = models.DecimalField(db_column='TOTSERV_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totfrete_nf_saida = models.DecimalField(db_column='TOTFRETE_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_nf_saida = models.NullBooleanField(db_column='CANC_NF_SAIDA')  # Field name made lowercase.
    base_nf_saida = models.TextField(db_column='BASE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    obs_nf_saida = models.TextField(db_column='OBS_NF_SAIDA')  # Field name made lowercase.
    compfrete_nf_saida = models.SmallIntegerField(db_column='COMPFRETE_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    alterar_nf_saida = models.NullBooleanField(db_column='ALTERAR_NF_SAIDA')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=100)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=28)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=36)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=38)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=100)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=40)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=40)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=60)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=4)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=18)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=4)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=18)  # Field name made lowercase.
    ramal1_cli = models.CharField(db_column='RAMAL1_CLI', max_length=20)  # Field name made lowercase.
    nf_conj = models.NullBooleanField(db_column='NF_CONJ')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_subst_tributaria = models.DecimalField(db_column='BASE_SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_nf_saida = models.NullBooleanField(db_column='DESCSUFRAMA_NF_SAIDA')  # Field name made lowercase.
    val_icms = models.DecimalField(db_column='VAL_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_saida = models.DecimalField(db_column='IPI_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total_nf_saida = models.DecimalField(db_column='TOTAL_NF_SAIDA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    user_nf = models.CharField(db_column='USER_NF', max_length=50)  # Field name made lowercase.
    serie_nf = models.IntegerField(db_column='SERIE_NF', blank=True, null=True)  # Field name made lowercase.
    cod_sit_nf = models.CharField(db_column='COD_SIT_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_mod_nf = models.CharField(db_column='COD_MOD_NF', max_length=2, blank=True, null=True)  # Field name made lowercase.
    chave_nf = models.TextField(db_column='CHAVE_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_FISCAIS_MIDIA'


class NotasReferenciaRetorno(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde = models.BigIntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NOTAS_REFERENCIA_RETORNO'


class NumConhecimentos(models.Model):
    faixai_num = models.BigIntegerField(db_column='faixaI_num', blank=True, null=True)  # Field name made lowercase.
    faixaf_num = models.BigIntegerField(db_column='faixaF_num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Num_Conhecimentos'


class NumConhecimentos2(models.Model):
    faixai_num = models.CharField(db_column='faixaI_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.
    faixaf_num = models.CharField(db_column='faixaF_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Num_Conhecimentos2'


class NumConhecimentos3(models.Model):
    faixai_num = models.BigIntegerField(db_column='faixaI_num', blank=True, null=True)  # Field name made lowercase.
    faixaf_num = models.BigIntegerField(db_column='faixaF_num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Num_Conhecimentos3'


class NumConhecimentos4(models.Model):
    faixai_num = models.CharField(db_column='faixaI_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.
    faixaf_num = models.CharField(db_column='faixaF_Num', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Num_Conhecimentos4'


class Operacoes(models.Model):
    cod_oper = models.BigIntegerField(db_column='COD_OPER', primary_key=True)  # Field name made lowercase.
    desc_oper = models.CharField(db_column='DESC_OPER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPERACOES'


class Orcamentos(models.Model):
    cod_orca = models.BigIntegerField(db_column='COD_ORCA', primary_key=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_conta = models.IntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.ForeignKey(Funcionarios, models.DO_NOTHING, db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    data_orca = models.DateTimeField(db_column='DATA_ORCA', blank=True, null=True)  # Field name made lowercase.
    valid_orca = models.DateTimeField(db_column='VALID_ORCA', blank=True, null=True)  # Field name made lowercase.
    status_orca = models.CharField(db_column='STATUS_ORCA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_pagto = models.ForeignKey('TipoPagto', models.DO_NOTHING, db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.ForeignKey(FormaPagto, models.DO_NOTHING, db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.ForeignKey(Entregas, models.DO_NOTHING, db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    obs_orca = models.TextField(db_column='OBS_ORCA', blank=True, null=True)  # Field name made lowercase.
    tot_orca = models.DecimalField(db_column='TOT_ORCA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_orca = models.DecimalField(db_column='FRETE_ORCA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mult_orca = models.BooleanField(db_column='MULT_ORCA')  # Field name made lowercase.
    nf_orca = models.BooleanField(db_column='NF_ORCA')  # Field name made lowercase.
    pesoprod_orca = models.FloatField(db_column='PESOPROD_ORCA', blank=True, null=True)  # Field name made lowercase.
    pagafrete_orca = models.CharField(db_column='PAGAFRETE_ORCA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    troca_orca = models.BooleanField(db_column='TROCA_ORCA')  # Field name made lowercase.
    codostroca_orca = models.IntegerField(db_column='CODOSTROCA_ORCA', blank=True, null=True)  # Field name made lowercase.
    requis_orca = models.BooleanField(db_column='REQUIS_ORCA')  # Field name made lowercase.
    bv_orca = models.IntegerField(db_column='BV_ORCA', blank=True, null=True)  # Field name made lowercase.
    obsbv_orca = models.TextField(db_column='OBSBV_ORCA', blank=True, null=True)  # Field name made lowercase.
    data_aprov_amostra = models.DateTimeField(blank=True, null=True)
    dt_alt_cad = models.DateTimeField(db_column='DT_ALT_CAD', blank=True, null=True)  # Field name made lowercase.
    cod_caixa = models.BigIntegerField(db_column='COD_CAIXA', blank=True, null=True)  # Field name made lowercase.
    enviou = models.NullBooleanField(db_column='ENVIOU')  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_orca = models.NullBooleanField(db_column='DESCSUFRAMA_ORCA')  # Field name made lowercase.
    empresa_orca = models.CharField(db_column='EMPRESA_ORCA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tiposubst_orca = models.CharField(db_column='TIPOSUBST_ORCA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORCAMENTOS'


class Os(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', primary_key=True)  # Field name made lowercase.
    cod_orca = models.ForeignKey(Orcamentos, models.DO_NOTHING, db_column='COD_ORCA')  # Field name made lowercase.
    cod_cli = models.IntegerField(db_column='COD_CLI')  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND')  # Field name made lowercase.
    cod_coord = models.IntegerField(db_column='COD_COORD', blank=True, null=True)  # Field name made lowercase.
    data1_os = models.DateTimeField(db_column='DATA1_OS', blank=True, null=True)  # Field name made lowercase.
    data2_os = models.DateTimeField(db_column='DATA2_OS', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.ForeignKey(Entregas, models.DO_NOTHING, db_column='COD_ENT')  # Field name made lowercase.
    obs_os = models.TextField(db_column='OBS_OS', blank=True, null=True)  # Field name made lowercase.
    tot_os = models.DecimalField(db_column='TOT_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_os = models.DecimalField(db_column='FRETE_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    canc_os = models.NullBooleanField(db_column='CANC_OS')  # Field name made lowercase.
    motivcanc_os = models.TextField(db_column='MOTIVCANC_OS', blank=True, null=True)  # Field name made lowercase.
    altera_os = models.NullBooleanField(db_column='ALTERA_OS')  # Field name made lowercase.
    altera_obs = models.NullBooleanField(db_column='ALTERA_OBS')  # Field name made lowercase.
    nf_os = models.BooleanField(db_column='NF_OS')  # Field name made lowercase.
    pagafrete_os = models.CharField(db_column='PAGAFRETE_OS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pesoprod_os = models.FloatField(db_column='PESOPROD_OS', blank=True, null=True)  # Field name made lowercase.
    qtdevolume_os = models.BigIntegerField(db_column='QTDEVOLUME_OS', blank=True, null=True)  # Field name made lowercase.
    volume_os = models.FloatField(db_column='VOLUME_OS', blank=True, null=True)  # Field name made lowercase.
    voltaetq_os = models.NullBooleanField(db_column='VOLTAETQ_OS')  # Field name made lowercase.
    troca_os = models.NullBooleanField(db_column='TROCA_OS')  # Field name made lowercase.
    codostroca_os = models.IntegerField(db_column='CODOSTROCA_OS', blank=True, null=True)  # Field name made lowercase.
    tottroca_os = models.DecimalField(db_column='TOTTROCA_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    liberadovend_os = models.NullBooleanField(db_column='LIBERADOVEND_OS')  # Field name made lowercase.
    requis_os = models.BooleanField(db_column='REQUIS_OS')  # Field name made lowercase.
    hora_libera_os = models.DateTimeField(db_column='HORA_LIBERA_OS', blank=True, null=True)  # Field name made lowercase.
    cod_conta = models.IntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    bv_os = models.IntegerField(db_column='BV_OS', blank=True, null=True)  # Field name made lowercase.
    obsbv_os = models.TextField(db_column='OBSBV_OS', blank=True, null=True)  # Field name made lowercase.
    info_os = models.NullBooleanField(db_column='INFO_OS')  # Field name made lowercase.
    dataos_prev_li = models.DateTimeField(db_column='DATAOS_PREV_LI', blank=True, null=True)  # Field name made lowercase.
    data_limite = models.DateTimeField(db_column='DATA_LIMITE', blank=True, null=True)  # Field name made lowercase.
    cod_ent2 = models.BigIntegerField(db_column='COD_ENT2', blank=True, null=True)  # Field name made lowercase.
    dt_alt_cad = models.DateTimeField(db_column='DT_ALT_CAD', blank=True, null=True)  # Field name made lowercase.
    cod_caixa = models.BigIntegerField(db_column='COD_CAIXA', blank=True, null=True)  # Field name made lowercase.
    numcopia_os = models.BigIntegerField(db_column='NUMCOPIA_OS', blank=True, null=True)  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tiposubst_os = models.CharField(db_column='TIPOSUBST_OS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    descsuframa_os = models.NullBooleanField(db_column='DESCSUFRAMA_OS')  # Field name made lowercase.
    cod_contrato = models.BigIntegerField(db_column='COD_CONTRATO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS'


class OsCf(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    data_aut = models.DateTimeField(db_column='DATA_AUT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_CF'


class OsConhecimento(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    numcorr_os = models.BigIntegerField(blank=True, null=True)
    ativo_conhecimento = models.NullBooleanField(db_column='Ativo_conhecimento')  # Field name made lowercase.
    volume_os = models.IntegerField(db_column='Volume_Os', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_Conhecimento'


class OsConhecimento2(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    numcorr_os = models.CharField(max_length=10, blank=True, null=True)
    ativo_conhecimento = models.NullBooleanField(db_column='Ativo_conhecimento')  # Field name made lowercase.
    volume_os = models.IntegerField(db_column='Volume_Os', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_Conhecimento2'


class OsConhecimento3(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    numcorr_os = models.BigIntegerField(blank=True, null=True)
    ativo_conhecimento = models.NullBooleanField(db_column='Ativo_conhecimento')  # Field name made lowercase.
    volume_os = models.IntegerField(db_column='Volume_Os', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_Conhecimento3'


class OsConhecimento4(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    numcorr_os = models.CharField(max_length=10, blank=True, null=True)
    ativo_conhecimento = models.NullBooleanField(db_column='Ativo_conhecimento')  # Field name made lowercase.
    volume_os = models.IntegerField(db_column='Volume_Os', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_Conhecimento4'


class OsEmpresa(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', primary_key=True)  # Field name made lowercase.
    empresa_os = models.CharField(db_column='EMPRESA_OS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    quemconf_os = models.CharField(db_column='QUEMCONF_OS', max_length=40, blank=True, null=True)  # Field name made lowercase.
    autorizado = models.NullBooleanField(db_column='AUTORIZADO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_EMPRESA'


class OsFreteextra(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    valor_freteextra = models.DecimalField(db_column='VALOR_FRETEEXTRA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desc_freteextra = models.TextField(db_column='DESC_FRETEEXTRA', blank=True, null=True)  # Field name made lowercase.
    paga_freteextra = models.CharField(db_column='PAGA_FRETEEXTRA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_FRETEEXTRA'


class OsNf(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS')  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    ativo_os_nf = models.BooleanField(db_column='ATIVO_OS_NF')  # Field name made lowercase.
    pagto_conf = models.NullBooleanField(db_column='PAGTO_CONF')  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    modelo_nf = models.CharField(db_column='MODELO_NF', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_NF'


class OsObsextra(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    desc_obsextra = models.TextField(db_column='DESC_OBSEXTRA', blank=True, null=True)  # Field name made lowercase.
    tipo_obsextra = models.CharField(db_column='TIPO_OBSEXTRA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_OBSEXTRA'


class OsRisco(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    risco_os = models.CharField(db_column='RISCO_OS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    desaprovado_os = models.NullBooleanField(db_column='DESAPROVADO_OS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OS_RISCO'


class Pais(models.Model):
    cod = models.IntegerField(primary_key=True)
    pais = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PAIS'


class PedCompra(models.Model):
    cod_cmp = models.BigIntegerField(db_column='COD_CMP', primary_key=True)  # Field name made lowercase.
    cod_forn = models.ForeignKey(Fornecedores, models.DO_NOTHING, db_column='COD_FORN')  # Field name made lowercase.
    status_cmp = models.CharField(db_column='STATUS_CMP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data1_cmp = models.DateTimeField(db_column='DATA1_CMP', blank=True, null=True)  # Field name made lowercase.
    data2_cmp = models.DateTimeField(db_column='DATA2_CMP', blank=True, null=True)  # Field name made lowercase.
    prev_cmp = models.DateTimeField(db_column='PREV_CMP', blank=True, null=True)  # Field name made lowercase.
    val_icms = models.IntegerField(db_column='VAL_ICMS', blank=True, null=True)  # Field name made lowercase.
    taxa_cmp = models.DecimalField(db_column='TAXA_CMP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_cmp = models.TextField(db_column='OBS_CMP', blank=True, null=True)  # Field name made lowercase.
    priori_cmp = models.CharField(db_column='PRIORI_CMP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    criado_cmp = models.CharField(db_column='CRIADO_CMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    solicitado_cmp = models.CharField(db_column='SOLICITADO_CMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    alterado_cmp = models.NullBooleanField(db_column='ALTERADO_CMP')  # Field name made lowercase.
    empresa_cmp = models.CharField(db_column='EMPRESA_CMP', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PED_COMPRA'


class PedCompraNf(models.Model):
    cod_cmp = models.BigIntegerField(db_column='COD_CMP')  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PED_COMPRA_NF'


class PedCompraServ(models.Model):
    cod_cmp = models.BigIntegerField(db_column='COD_CMP', primary_key=True)  # Field name made lowercase.
    cod_pserv = models.BigIntegerField(db_column='COD_PSERV')  # Field name made lowercase.
    data1_cmp = models.DateTimeField(db_column='DATA1_CMP', blank=True, null=True)  # Field name made lowercase.
    data2_cmp = models.DateTimeField(db_column='DATA2_CMP', blank=True, null=True)  # Field name made lowercase.
    prev_cmp = models.DateTimeField(db_column='PREV_CMP', blank=True, null=True)  # Field name made lowercase.
    cod_pagto = models.IntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_frmpagto = models.IntegerField(db_column='COD_FRMPAGTO', blank=True, null=True)  # Field name made lowercase.
    taxa_cmp = models.DecimalField(db_column='TAXA_CMP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    obs_cmp = models.TextField(db_column='OBS_CMP', blank=True, null=True)  # Field name made lowercase.
    priori_cmp = models.CharField(db_column='PRIORI_CMP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    criado_cmp = models.CharField(db_column='CRIADO_CMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    solicitado_cmp = models.CharField(db_column='SOLICITADO_CMP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    alterado_cmp = models.NullBooleanField(db_column='ALTERADO_CMP')  # Field name made lowercase.
    empresa_cmp = models.CharField(db_column='EMPRESA_CMP', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PED_COMPRA_SERV'


class PedCompraTrocas(models.Model):
    cod_cmp = models.BigIntegerField(db_column='COD_CMP')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    qtde_trc = models.BigIntegerField(db_column='QTDE_TRC', blank=True, null=True)  # Field name made lowercase.
    valor_trc = models.DecimalField(db_column='VALOR_TRC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PED_COMPRA_TROCAS'


class PerguntasMercado(models.Model):
    cod_mercado = models.ForeignKey(Mercados, models.DO_NOTHING, db_column='cod_mercado')
    desc_pergunta = models.CharField(max_length=50, blank=True, null=True)
    tipo_pergunta = models.DecimalField(max_digits=18, decimal_places=0)
    num_pergunta = models.DecimalField(max_digits=18, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'PERGUNTAS_MERCADO'
        unique_together = (('cod_mercado', 'tipo_pergunta', 'num_pergunta'),)


class Pis(models.Model):
    cfop_nf_saida = models.CharField(db_column='CFOP_NF_SAIDA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sittrib_nf_saida = models.CharField(db_column='SITTRIB_NF_SAIDA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pis_nf_saida = models.CharField(db_column='PIS_NF_SAIDA', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PIS'


class Plantao(models.Model):
    data = models.DateTimeField(db_column='DATA', primary_key=True)  # Field name made lowercase.
    plantonista = models.CharField(db_column='PLANTONISTA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLANTAO'


class PrecosEsedex(models.Model):
    peso_ini = models.BigIntegerField(db_column='PESO_INI', blank=True, null=True)  # Field name made lowercase.
    peso_fim = models.BigIntegerField(db_column='PESO_FIM', blank=True, null=True)  # Field name made lowercase.
    grandesp = models.DecimalField(db_column='GRANDESP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estadualsp = models.DecimalField(db_column='ESTADUALSP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprrjsc = models.DecimalField(db_column='MGPRRJSC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprrjsc_int = models.DecimalField(db_column='MGPRRJSC_INT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs = models.DecimalField(db_column='DFESGOMSRS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs_int = models.DecimalField(db_column='DFESGOMSRS_INT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    albamtpbpeseto = models.DecimalField(db_column='ALBAMTPBPESETO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    albamtpbpeseto_int = models.DecimalField(db_column='ALBAMTPBPESETO_INT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amcemapapirn = models.DecimalField(db_column='AMCEMAPAPIRN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amcemapapirn_int = models.DecimalField(db_column='AMCEMAPAPIRN_INT', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRECOS_ESEDEX'


class PrecosLaercio(models.Model):
    peso_ini = models.BigIntegerField(db_column='PESO_INI', blank=True, null=True)  # Field name made lowercase.
    peso_fim = models.BigIntegerField(db_column='PESO_FIM', blank=True, null=True)  # Field name made lowercase.
    capital_sp_hj = models.DecimalField(db_column='CAPITAL_SP_HJ', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    grande_sp_hj = models.DecimalField(db_column='GRANDE_SP_HJ', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    capital_sp_24 = models.DecimalField(db_column='CAPITAL_SP_24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    grande_sp_24 = models.DecimalField(db_column='GRANDE_SP_24', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRECOS_LAERCIO'


class PrecosModificados(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    desc_prod = models.CharField(db_column='DESC_PROD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc_serv = models.CharField(db_column='DESC_SERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    valor_pre = models.FloatField(db_column='VALOR_PRE', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRECOS_MODIFICADOS'


class PrecosProd(models.Model):
    cod_prod = models.ForeignKey('Produtos', models.DO_NOTHING, db_column='COD_PROD')  # Field name made lowercase.
    qtde_pre = models.BigIntegerField(db_column='QTDE_PRE')  # Field name made lowercase.
    valor_pre = models.DecimalField(db_column='VALOR_PRE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imp_pre = models.DecimalField(db_column='IMP_PRE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lucro_pre = models.FloatField(db_column='LUCRO_PRE', blank=True, null=True)  # Field name made lowercase.
    taxa_pre = models.FloatField(db_column='TAXA_PRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRECOS_PROD'
        unique_together = (('cod_prod', 'qtde_pre'),)


class PrecosServ(models.Model):
    cod_serv = models.ForeignKey('Servicos', models.DO_NOTHING, db_column='COD_SERV')  # Field name made lowercase.
    qtde_pre = models.BigIntegerField(db_column='QTDE_PRE')  # Field name made lowercase.
    valor_pre = models.DecimalField(db_column='VALOR_PRE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imp_pre = models.DecimalField(db_column='IMP_PRE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRECOS_SERV'
        unique_together = (('cod_serv', 'qtde_pre'),)


class PrecosTotal(models.Model):
    peso_ini = models.BigIntegerField(db_column='PESO_INI', blank=True, null=True)  # Field name made lowercase.
    peso_fim = models.BigIntegerField(db_column='PESO_FIM', blank=True, null=True)  # Field name made lowercase.
    localsp = models.DecimalField(db_column='LocalSP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rj = models.DecimalField(db_column='RJ', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprsc = models.DecimalField(db_column='MGPRSC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs = models.DecimalField(db_column='DFESGOMSRS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bamttoalse = models.DecimalField(db_column='BAMTTOALSE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pbpepi = models.DecimalField(db_column='PBPEPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    accemaparn = models.DecimalField(db_column='ACCEMAPARN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    int_sp = models.DecimalField(db_column='INT_SP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    int_sprjmg = models.DecimalField(db_column='INT_SPRJMG', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    int_scprrs = models.DecimalField(db_column='INT_SCPRRS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_sp = models.DecimalField(db_column='RED_SP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_rj = models.DecimalField(db_column='RED_RJ', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_mgprsc = models.DecimalField(db_column='RED_MGPRSC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_dfesgomsrs = models.DecimalField(db_column='RED_DFESGOMSRS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_bamttoalse = models.DecimalField(db_column='RED_BAMTTOALSE', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_pbpepiro = models.DecimalField(db_column='RED_PBPEPIRO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_acapamcemaparn = models.DecimalField(db_column='RED_ACAPAMCEMAPARN', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    red_rr = models.DecimalField(db_column='RED_RR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRECOS_TOTAL'


class PrestaServ(models.Model):
    cod_pserv = models.BigIntegerField(db_column='COD_PSERV', primary_key=True)  # Field name made lowercase.
    nome_pserv = models.CharField(db_column='NOME_PSERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contato_pserv = models.CharField(db_column='CONTATO_PSERV', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_pserv = models.CharField(db_column='EMAIL_PSERV', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cnpj_pserv = models.CharField(db_column='CNPJ_PSERV', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_pserv = models.CharField(db_column='IE_PSERV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    end_pserv = models.CharField(db_column='END_PSERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_pserv = models.CharField(db_column='NUM_PSERV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_pserv = models.CharField(db_column='BAIR_PSERV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_pserv = models.CharField(db_column='CID_PSERV', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_pserv = models.CharField(db_column='EST_PSERV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_pserv = models.CharField(db_column='CEP_PSERV', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd1_pserv = models.CharField(db_column='DDD1_PSERV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_pserv = models.CharField(db_column='TEL1_PSERV', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal1_pserv = models.CharField(db_column='RAMAL1_PSERV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ddd2_pserv = models.CharField(db_column='DDD2_PSERV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_pserv = models.CharField(db_column='TEL2_PSERV', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal2_pserv = models.CharField(db_column='RAMAL2_PSERV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dddfax_pserv = models.CharField(db_column='DDDFAX_PSERV', max_length=2, blank=True, null=True)  # Field name made lowercase.
    fax_pserv = models.CharField(db_column='FAX_PSERV', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramalfax_pserv = models.CharField(db_column='RAMALFAX_PSERV', max_length=10, blank=True, null=True)  # Field name made lowercase.
    obs_pserv = models.TextField(db_column='OBS_PSERV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTA_SERV'


class PrestaServServ(models.Model):
    cod_pserv = models.BigIntegerField(db_column='COD_PSERV')  # Field name made lowercase.
    cod_serv_presta = models.BigIntegerField(db_column='COD_SERV_PRESTA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRESTA_SERV_SERV'


class ProducaoOs(models.Model):
    cod_os = models.ForeignKey(Os, models.DO_NOTHING, db_column='COD_OS')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    data_tar = models.DateTimeField(db_column='DATA_TAR', blank=True, null=True)  # Field name made lowercase.
    qtde_tar = models.IntegerField(db_column='QTDE_TAR', blank=True, null=True)  # Field name made lowercase.
    obs_os = models.TextField(db_column='OBS_OS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUCAO_OS'
        unique_together = (('cod_os', 'cod_prod', 'cod_serv'),)


class Produtos(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', primary_key=True)  # Field name made lowercase.
    desc_prod = models.CharField(db_column='DESC_PROD', max_length=300, blank=True, null=True)  # Field name made lowercase.
    min_prod = models.IntegerField(db_column='MIN_PROD', blank=True, null=True)  # Field name made lowercase.
    saldo_prod = models.BigIntegerField(db_column='SALDO_PROD', blank=True, null=True)  # Field name made lowercase.
    teorico_prod = models.BigIntegerField(db_column='TEORICO_PROD', blank=True, null=True)  # Field name made lowercase.
    custoref_prod = models.DecimalField(db_column='CUSTOREF_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    custo_prod = models.DecimalField(db_column='CUSTO_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    med_prod = models.DecimalField(db_column='MED_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cod_cat = models.CharField(db_column='COD_CAT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    peso_prod = models.FloatField(db_column='PESO_PROD', blank=True, null=True)  # Field name made lowercase.
    base_prod = models.FloatField(db_column='BASE_PROD', blank=True, null=True)  # Field name made lowercase.
    altura_prod = models.FloatField(db_column='ALTURA_PROD', blank=True, null=True)  # Field name made lowercase.
    largura_prod = models.FloatField(db_column='LARGURA_PROD', blank=True, null=True)  # Field name made lowercase.
    obs_prod = models.TextField(db_column='OBS_PROD', blank=True, null=True)  # Field name made lowercase.
    capaci_prod = models.CharField(db_column='CAPACI_PROD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    caract_prod = models.CharField(db_column='CARACT_PROD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    naomostra_prod = models.NullBooleanField(db_column='NAOMOSTRA_PROD')  # Field name made lowercase.
    minloja_prod = models.FloatField(db_column='MINLOJA_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_mar = models.BigIntegerField(db_column='COD_MAR', blank=True, null=True)  # Field name made lowercase.
    obs2_prod = models.TextField(db_column='OBS2_PROD', blank=True, null=True)  # Field name made lowercase.
    datacadastro_prod = models.DateTimeField(db_column='DATACADASTRO_PROD', blank=True, null=True)  # Field name made lowercase.
    codfreq_prod = models.IntegerField(db_column='CODFREQ_PROD', blank=True, null=True)  # Field name made lowercase.
    coddia_prod = models.IntegerField(db_column='CODDIA_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_fabri = models.CharField(db_column='COD_FABRI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    capaci_prod2 = models.BigIntegerField(db_column='CAPACI_PROD2', blank=True, null=True)  # Field name made lowercase.
    cod_supercat = models.BigIntegerField(db_column='COD_SUPERCAT', blank=True, null=True)  # Field name made lowercase.
    naomostra_loja = models.NullBooleanField(db_column='NAOMOSTRA_LOJA')  # Field name made lowercase.
    data_minimo = models.DateTimeField(db_column='DATA_MINIMO', blank=True, null=True)  # Field name made lowercase.
    lista_etq = models.NullBooleanField(db_column='LISTA_ETQ')  # Field name made lowercase.
    porcaixa_prod = models.FloatField(db_column='PORCAIXA_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_barras = models.CharField(db_column='COD_BARRAS', max_length=25, blank=True, null=True)  # Field name made lowercase.
    data_cad = models.DateTimeField(db_column='DATA_CAD', blank=True, null=True)  # Field name made lowercase.
    resp_prod = models.BigIntegerField(db_column='RESP_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_grupo = models.BigIntegerField(db_column='COD_GRUPO', blank=True, null=True)  # Field name made lowercase.
    inativo_grupo = models.NullBooleanField(db_column='INATIVO_GRUPO')  # Field name made lowercase.
    saldo_ant_cr = models.BigIntegerField(db_column='SALDO_ANT_CR', blank=True, null=True)  # Field name made lowercase.
    multi_prod = models.BigIntegerField(db_column='MULTI_PROD', blank=True, null=True)  # Field name made lowercase.
    reserv_prod = models.BigIntegerField(db_column='RESERV_PROD', blank=True, null=True)  # Field name made lowercase.
    classitrib_prod = models.CharField(db_column='CLASSITRIB_PROD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    monitora_prod = models.NullBooleanField(db_column='MONITORA_PROD')  # Field name made lowercase.
    vitrine_prod = models.NullBooleanField(db_column='VITRINE_PROD')  # Field name made lowercase.
    icms_reduzido = models.NullBooleanField(db_column='ICMS_REDUZIDO')  # Field name made lowercase.
    saldo_dep = models.BigIntegerField(db_column='SALDO_DEP', blank=True, null=True)  # Field name made lowercase.
    monitora2_prod = models.NullBooleanField(db_column='MONITORA2_PROD')  # Field name made lowercase.
    crdesatualizado_prod = models.NullBooleanField(db_column='CRDESATUALIZADO_PROD')  # Field name made lowercase.
    importado_prod = models.NullBooleanField(db_column='IMPORTADO_PROD')  # Field name made lowercase.
    ipi_prod = models.FloatField(db_column='IPI_PROD', blank=True, null=True)  # Field name made lowercase.
    cxfechada_prod = models.CharField(db_column='CxFechada_prod', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tag_prod = models.CharField(db_column='TAG_PROD', max_length=256, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(max_length=256, blank=True, null=True)
    descloja_prod = models.CharField(db_column='DESCLOJA_PROD', max_length=256, blank=True, null=True)  # Field name made lowercase.
    categoria_web = models.TextField(db_column='CATEGORIA_WEB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sub_categoria_web = models.TextField(db_column='SUB_CATEGORIA_WEB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PRODUTOS'


class ProdutosCategoria(models.Model):
    cod_cat = models.DecimalField(max_digits=18, decimal_places=0)
    cod_prod = models.CharField(max_length=50)
    prioridade_cat = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PRODUTOS_CATEGORIA'
        unique_together = (('cod_cat', 'cod_prod'),)


class ProdutosExpedicao(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    minimo = models.BigIntegerField(db_column='MINIMO', blank=True, null=True)  # Field name made lowercase.
    completo = models.BigIntegerField(db_column='COMPLETO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTOS_EXPEDICAO'


class ProdutosImport(models.Model):
    cod_dia = models.IntegerField(db_column='COD_DIA', primary_key=True)  # Field name made lowercase.
    desc_dia = models.CharField(db_column='DESC_DIA', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTOS_IMPORT'


class ProdutosImportados(models.Model):
    cod_imp = models.BigIntegerField(db_column='COD_IMP', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde_inserida = models.BigIntegerField(db_column='QTDE_INSERIDA', blank=True, null=True)  # Field name made lowercase.
    qtde_ativo = models.BigIntegerField(db_column='QTDE_ATIVO', blank=True, null=True)  # Field name made lowercase.
    data_inserida = models.DateTimeField(db_column='DATA_INSERIDA', blank=True, null=True)  # Field name made lowercase.
    importado = models.NullBooleanField(db_column='IMPORTADO')  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    valor_prod = models.DecimalField(db_column='VALOR_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTOS_IMPORTADOS'


class ProdutosMemorando(models.Model):
    cod_prod = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='COD_PROD', primary_key=True)  # Field name made lowercase.
    mem_prod = models.TextField(db_column='MEM_PROD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTOS_MEMORANDO'


class ProdutosQtde(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde_tech = models.BigIntegerField(db_column='QTDE_TECH', blank=True, null=True)  # Field name made lowercase.
    qtde_midia = models.BigIntegerField(db_column='QTDE_MIDIA', blank=True, null=True)  # Field name made lowercase.
    qtde_data = models.BigIntegerField(db_column='QTDE_DATA', blank=True, null=True)  # Field name made lowercase.
    teorico_tech = models.BigIntegerField(db_column='TEORICO_TECH', blank=True, null=True)  # Field name made lowercase.
    teorico_midia = models.BigIntegerField(db_column='TEORICO_MIDIA', blank=True, null=True)  # Field name made lowercase.
    teorico_data = models.BigIntegerField(db_column='TEORICO_DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODUTOS_QTDE'


class ProdMarcas(models.Model):
    cod_mar = models.BigIntegerField(db_column='COD_MAR', primary_key=True)  # Field name made lowercase.
    desc_mar = models.CharField(db_column='DESC_MAR', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROD_MARCAS'


class ProgramacaoSilk(models.Model):
    cod_prog = models.BigIntegerField(db_column='COD_PROG', blank=True, null=True)  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_priori = models.BigIntegerField(db_column='COD_PRIORI', blank=True, null=True)  # Field name made lowercase.
    data_prog = models.DateTimeField(db_column='DATA_PROG', blank=True, null=True)  # Field name made lowercase.
    dataprev_prog = models.DateTimeField(db_column='DATAPREV_PROG', blank=True, null=True)  # Field name made lowercase.
    desc_prog = models.TextField(db_column='DESC_PROG', blank=True, null=True)  # Field name made lowercase.
    status_prog = models.CharField(db_column='STATUS_PROG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    usersol_prog = models.CharField(db_column='USERSOL_PROG', max_length=60, blank=True, null=True)  # Field name made lowercase.
    useralt_prog = models.CharField(db_column='USERALT_PROG', max_length=60, blank=True, null=True)  # Field name made lowercase.
    userfim_prog = models.CharField(db_column='USERFIM_PROG', max_length=60, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROGRAMACAO_SILK'


class ProCategorias(models.Model):
    cat_codigo = models.CharField(db_column='Cat_Codigo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cod_supercat = models.CharField(db_column='Cod_SuperCat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cat_apelido = models.CharField(db_column='Cat_Apelido', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cat_descricao = models.CharField(db_column='Cat_Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cat_mostrar = models.BooleanField(db_column='Cat_Mostrar')  # Field name made lowercase.
    cat_tipo = models.CharField(db_column='Cat_Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pro_Categorias'


class Qtde(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    desc_prod = models.TextField(db_column='DESC_PROD', blank=True, null=True)  # Field name made lowercase.
    qtde = models.BigIntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    ano = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'QTDE'


class Receitas(models.Model):
    cod_receita = models.BigIntegerField(db_column='COD_RECEITA', primary_key=True)  # Field name made lowercase.
    desc_receita = models.CharField(db_column='DESC_RECEITA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cod_catrec = models.ForeignKey(CategoriasRec, models.DO_NOTHING, db_column='COD_CATREC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECEITAS'


class Redf(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='Cod_NF_Saida', blank=True, null=True)  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='Empresa_NF_Saida', max_length=1, blank=True, null=True)  # Field name made lowercase.
    inc_redf = models.NullBooleanField(db_column='Inc_REDF')  # Field name made lowercase.
    canc_redf = models.NullBooleanField(db_column='Canc_REDF')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REDF'


class RelEtiq(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS')  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contato_cli = models.CharField(db_column='CONTATO_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    departamento_conta = models.CharField(db_column='DEPARTAMENTO_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REL_ETIQ'


class RequisMaterial(models.Model):
    cod_requis = models.BigIntegerField(db_column='COD_REQUIS', primary_key=True)  # Field name made lowercase.
    finalidade_requis = models.CharField(db_column='FINALIDADE_REQUIS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    tipo_requis = models.CharField(db_column='TIPO_REQUIS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    obs_requis = models.TextField(db_column='OBS_REQUIS', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.IntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.IntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    data_requis = models.DateTimeField(db_column='DATA_REQUIS', blank=True, null=True)  # Field name made lowercase.
    atendida_requis = models.BooleanField(db_column='ATENDIDA_REQUIS')  # Field name made lowercase.
    arquivo_requis = models.CharField(db_column='ARQUIVO_REQUIS', max_length=80, blank=True, null=True)  # Field name made lowercase.
    autoriza_requis = models.CharField(db_column='AUTORIZA_REQUIS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    quem_autoriza = models.CharField(db_column='QUEM_AUTORIZA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    data_autoriza = models.DateTimeField(db_column='DATA_AUTORIZA', blank=True, null=True)  # Field name made lowercase.
    empresa_requis = models.CharField(db_column='EMPRESA_REQUIS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_contrato = models.BigIntegerField(db_column='COD_CONTRATO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REQUIS_MATERIAL'


class RequisNf(models.Model):
    cod_requis = models.BigIntegerField(db_column='COD_REQUIS')  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    empresa_nf_saida = models.CharField(db_column='EMPRESA_NF_SAIDA', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REQUIS_NF'


class Reservas(models.Model):
    cod_reserv = models.BigIntegerField(db_column='COD_RESERV', primary_key=True)  # Field name made lowercase.
    cod_cli = models.IntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_os = models.IntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.IntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    valid_reserv = models.DateTimeField(db_column='VALID_RESERV', blank=True, null=True)  # Field name made lowercase.
    obs_reserv = models.TextField(db_column='OBS_RESERV', blank=True, null=True)  # Field name made lowercase.
    canc_reserv = models.BooleanField(db_column='CANC_RESERV')  # Field name made lowercase.
    exc_reserv = models.NullBooleanField(db_column='EXC_RESERV')  # Field name made lowercase.
    empresa_reserv = models.CharField(db_column='EMPRESA_RESERV', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVAS'


class RespostasMercado(models.Model):
    cod_mercado = models.DecimalField(max_digits=18, decimal_places=0)
    cod_pergunta = models.DecimalField(max_digits=18, decimal_places=0)
    cod_at = models.DecimalField(max_digits=18, decimal_places=0)
    resposta = models.CharField(max_length=15)
    obs_resposta = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RESPOSTAS_MERCADO'
        unique_together = (('cod_pergunta', 'cod_mercado', 'cod_at'),)


class RimageAtendimentos(models.Model):
    cod_atend = models.BigIntegerField(db_column='COD_ATEND', primary_key=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    data_atend = models.DateTimeField(db_column='DATA_ATEND', blank=True, null=True)  # Field name made lowercase.
    resp_atend = models.CharField(db_column='RESP_ATEND', max_length=30, blank=True, null=True)  # Field name made lowercase.
    tipo_atend = models.CharField(db_column='TIPO_ATEND', max_length=1, blank=True, null=True)  # Field name made lowercase.
    prob_atend = models.CharField(db_column='PROB_ATEND', max_length=200, blank=True, null=True)  # Field name made lowercase.
    proced_atend = models.TextField(db_column='PROCED_ATEND', blank=True, null=True)  # Field name made lowercase.
    contato_atend = models.CharField(db_column='CONTATO_ATEND', max_length=30, blank=True, null=True)  # Field name made lowercase.
    solu_atend = models.NullBooleanField(db_column='SOLU_ATEND')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RIMAGE_ATENDIMENTOS'


class Rma(models.Model):
    cod_rma = models.BigIntegerField(db_column='COD_RMA')  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_conta = models.IntegerField(db_column='COD_CONTA', blank=True, null=True)  # Field name made lowercase.
    cod_vend = models.BigIntegerField(db_column='COD_VEND', blank=True, null=True)  # Field name made lowercase.
    data_rma = models.DateTimeField(db_column='DATA_RMA', blank=True, null=True)  # Field name made lowercase.
    perdido_rma = models.NullBooleanField(db_column='PERDIDO_RMA')  # Field name made lowercase.
    analisado_rma = models.NullBooleanField(db_column='ANALISADO_RMA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RMA'


class Relatoriolojaprod(models.Model):
    cod_prod = models.TextField(blank=True, null=True)  # This field type is a guess.
    quantidade = models.FloatField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RelatorioLojaProd'


class SaldoProdJulho10(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    desc_prod = models.CharField(db_column='DESC_PROD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    saldo_prod = models.BigIntegerField(db_column='SALDO_PROD', blank=True, null=True)  # Field name made lowercase.
    cr_prod = models.DecimalField(db_column='CR_PROD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SALDO_PROD_JULHO10'


class Sedex10(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    metro_s10 = models.DecimalField(db_column='METRO_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    estadual_s10 = models.DecimalField(db_column='ESTADUAL_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rjmgprsc_s10 = models.DecimalField(db_column='RJMGPRSC_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rjmgprsc_int_s10 = models.DecimalField(db_column='RJMGPRSC_INT_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs_s10 = models.DecimalField(db_column='DFESGOMSRS_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesgomsrs_int_s10 = models.DecimalField(db_column='DFESGOMSRS_INT_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ba_s10 = models.DecimalField(db_column='BA_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ba_int_s10 = models.DecimalField(db_column='BA_INT_S10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEDEX_10'


class SedexConv(models.Model):
    faixai_peso = models.BigIntegerField(db_column='FAIXAI_PESO')  # Field name made lowercase.
    faixaf_peso = models.BigIntegerField(db_column='FAIXAF_PESO')  # Field name made lowercase.
    estado_sco = models.DecimalField(db_column='ESTADO_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprrjsc_sco = models.DecimalField(db_column='MGPRRJSC_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mgprrjsc_int_sco = models.DecimalField(db_column='MGPRRJSC_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesmsrs_sco = models.DecimalField(db_column='DFESMSRS_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dfesmsrs_int_sco = models.DecimalField(db_column='DFESMSRS_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    go_sco = models.DecimalField(db_column='GO_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    go_int_sco = models.DecimalField(db_column='GO_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bamtto_sco = models.DecimalField(db_column='BAMTTO_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bamtto_int_sco = models.DecimalField(db_column='BAMTTO_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alse_sco = models.DecimalField(db_column='ALSE_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    alse_int_sco = models.DecimalField(db_column='ALSE_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pbpepiro_sco = models.DecimalField(db_column='PBPEPIRO_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pbpepiro_int_sco = models.DecimalField(db_column='PBPEPIRO_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acapamcemaparn_sco = models.DecimalField(db_column='ACAPAMCEMAPARN_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    acapamcemaparn_int_sco = models.DecimalField(db_column='ACAPAMCEMAPARN_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rr_sco = models.DecimalField(db_column='RR_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rr_int_sco = models.DecimalField(db_column='RR_INT_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    local_sco = models.DecimalField(db_column='LOCAL_SCO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEDEX_CONV'


class SedexHoje(models.Model):
    peso_ini = models.IntegerField(db_column='Peso_INI')  # Field name made lowercase.
    peso_fin = models.IntegerField(db_column='Peso_FIN')  # Field name made lowercase.
    sp_local = models.DecimalField(db_column='SP_Local', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    sp_estadual = models.DecimalField(db_column='SP_Estadual', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rjmgpr = models.DecimalField(db_column='RJMGPR', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    df = models.DecimalField(db_column='DF', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SEDEX_HOJE'
        unique_together = (('peso_ini', 'peso_fin'),)


class Servicos(models.Model):
    cod_serv = models.BigIntegerField(db_column='COD_SERV', primary_key=True)  # Field name made lowercase.
    desc_serv = models.CharField(db_column='DESC_SERV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cod_catserv = models.ForeignKey(CategoriasServ, models.DO_NOTHING, db_column='COD_CATSERV', blank=True, null=True)  # Field name made lowercase.
    obs_serv = models.TextField(db_column='OBS_SERV', blank=True, null=True)  # Field name made lowercase.
    naomostra_serv = models.NullBooleanField(db_column='NAOMOSTRA_SERV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERVICOS'


class ServPrestaServ(models.Model):
    cod_serv_presta = models.BigIntegerField(db_column='COD_SERV_PRESTA', primary_key=True)  # Field name made lowercase.
    desc_serv_presta = models.CharField(db_column='DESC_SERV_PRESTA', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERV_PRESTA_SERV'


class SetorAtuacao(models.Model):
    cod_setor = models.IntegerField(db_column='COD_SETOR', primary_key=True)  # Field name made lowercase.
    desc_setor = models.CharField(db_column='DESC_SETOR', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SETOR_ATUACAO'


class SitdocNfeEntrada(models.Model):
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    desc_sit = models.CharField(db_column='DESC_SIT', max_length=80, blank=True, null=True)  # Field name made lowercase.
    data_sit = models.DateTimeField(db_column='DATA_SIT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SITDOC_NFE_ENTRADA'


class Skype(models.Model):
    data_skype = models.DateTimeField(db_column='DATA_SKYPE', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    destino_skype = models.CharField(db_column='DESTINO_SKYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.
    msg_skype = models.TextField(db_column='MSG_SKYPE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SKYPE'


class SolicitacaoCancOs(models.Model):
    cod_os = models.BigIntegerField(db_column='Cod_OS', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datahora = models.DateTimeField(db_column='DataHora', blank=True, null=True)  # Field name made lowercase.
    observacao = models.CharField(db_column='Observacao', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLICITACAO_CANC_OS'


class SolicitacaoProd(models.Model):
    cod_solicitacao = models.BigIntegerField(db_column='Cod_Solicitacao', primary_key=True)  # Field name made lowercase.
    desc_solicitacao = models.CharField(db_column='Desc_Solicitacao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    data_solicitacao = models.DateTimeField(db_column='Data_Solicitacao', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=10, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='Cod_Cli', blank=True, null=True)  # Field name made lowercase.
    prioridade = models.BigIntegerField(db_column='Prioridade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLICITACAO_PROD'


class SolicitacaoProdNacionalidade(models.Model):
    cod_solicitacao = models.BigIntegerField(db_column='Cod_Solicitacao', blank=True, null=True)  # Field name made lowercase.
    data_resposta = models.DateTimeField(db_column='Data_resposta', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=15, blank=True, null=True)  # Field name made lowercase.
    importado_prod = models.NullBooleanField(db_column='Importado_prod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLICITACAO_PROD_NACIONALIDADE'


class SolprazoServ(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.BigIntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    cod_func = models.BigIntegerField(db_column='COD_FUNC', blank=True, null=True)  # Field name made lowercase.
    data_sol = models.DateTimeField(db_column='DATA_SOL', blank=True, null=True)  # Field name made lowercase.
    prazo_sol = models.NullBooleanField(db_column='PRAZO_SOL')  # Field name made lowercase.
    prazonec_sol = models.DateTimeField(db_column='PRAZONEC_SOL', blank=True, null=True)  # Field name made lowercase.
    obs_sol = models.TextField(db_column='OBS_SOL', blank=True, null=True)  # Field name made lowercase.
    imp_sol = models.NullBooleanField(db_column='IMP_SOL')  # Field name made lowercase.
    qtdeimp_sol = models.BigIntegerField(db_column='QTDEIMP_SOL', blank=True, null=True)  # Field name made lowercase.
    grav_sol = models.NullBooleanField(db_column='GRAV_SOL')  # Field name made lowercase.
    matgrav_sol = models.CharField(db_column='MATGRAV_SOL', max_length=19, blank=True, null=True)  # Field name made lowercase.
    qtdegrav_sol = models.BigIntegerField(db_column='QTDEGRAV_SOL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLPRAZO_SERV'


class SolNfsilk(models.Model):
    cod_requis = models.ForeignKey(RequisMaterial, models.DO_NOTHING, db_column='Cod_Requis', primary_key=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='Cod_Cli')  # Field name made lowercase.
    cod_os = models.ForeignKey(Os, models.DO_NOTHING, db_column='Cod_OS')  # Field name made lowercase.
    cod_vend = models.ForeignKey(Funcionarios, models.DO_NOTHING, db_column='Cod_Vend')  # Field name made lowercase.
    atend_sol = models.BooleanField(db_column='Atend_Sol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOL_NFSILK'


class SolNfInterna(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL')  # Field name made lowercase.
    dt_sol = models.DateTimeField(db_column='DT_SOL')  # Field name made lowercase.
    tipo_sol = models.CharField(db_column='TIPO_SOL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    resp_sol = models.CharField(db_column='RESP_Sol', max_length=20)  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    status_sol = models.CharField(db_column='STATUS_SOL', max_length=2)  # Field name made lowercase.
    mov_etq = models.NullBooleanField(db_column='MOV_ETQ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOL_NF_INTERNA'


class SolNfRemessa(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', blank=True, null=True)  # Field name made lowercase.
    data_sol = models.DateTimeField(db_column='DATA_SOL', blank=True, null=True)  # Field name made lowercase.
    tipo_sol = models.CharField(db_column='TIPO_SOL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    status_sol = models.CharField(db_column='STATUS_SOL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    resp_sol = models.CharField(db_column='RESP_SOL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cod_cli = models.BigIntegerField(db_column='COD_CLI', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT', blank=True, null=True)  # Field name made lowercase.
    tipo_nf_sol = models.CharField(db_column='TIPO_NF_SOL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    empresa_sol = models.CharField(db_column='EMPRESA_SOL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOL_NF_REMESSA'


class SolNfSaida(models.Model):
    cod_sol = models.BigIntegerField(db_column='COD_SOL', primary_key=True)  # Field name made lowercase.
    cod_os = models.BigIntegerField(db_column='COD_OS')  # Field name made lowercase.
    dt_ini_sol = models.DateTimeField(db_column='DT_INI_SOL')  # Field name made lowercase.
    dt_fim_sol = models.DateTimeField(db_column='DT_FIM_SOL', blank=True, null=True)  # Field name made lowercase.
    quem_sol = models.CharField(db_column='QUEM_SOL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', blank=True, null=True)  # Field name made lowercase.
    status_sol = models.CharField(db_column='STATUS_SOL', max_length=2)  # Field name made lowercase.
    imp_sol = models.NullBooleanField(db_column='IMP_SOL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOL_NF_SAIDA'


class SolProdforamix(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli')  # Field name made lowercase.
    cod_aten = models.BigIntegerField(db_column='Cod_Aten')  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data')  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SOL_PRODFORAMIX'
        unique_together = (('cod_cli', 'cod_aten', 'data'),)


class SolProdmix(models.Model):
    cod_cli = models.BigIntegerField(db_column='Cod_Cli')  # Field name made lowercase.
    cod_aten = models.BigIntegerField(db_column='Cod_Aten')  # Field name made lowercase.
    cod_prod = models.ForeignKey(Produtos, models.DO_NOTHING, db_column='Cod_Prod')  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data')  # Field name made lowercase.
    obs = models.TextField(db_column='Obs', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qtde = models.IntegerField(db_column='Qtde', blank=True, null=True)  # Field name made lowercase.
    fase = models.CharField(db_column='Fase', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sol = models.BigIntegerField(db_column='Cod_sol', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOL_PRODMIX'
        unique_together = (('cod_cli', 'cod_aten', 'cod_prod', 'data'),)


class SubstituicaoTributaria(models.Model):
    cod_subst = models.BigIntegerField(db_column='COD_SUBST', blank=True, null=True)  # Field name made lowercase.
    revenda_subst = models.FloatField(db_column='REVENDA_SUBST', blank=True, null=True)  # Field name made lowercase.
    consumo_subst = models.FloatField(db_column='CONSUMO_SUBST', blank=True, null=True)  # Field name made lowercase.
    cod_ct_prod = models.BigIntegerField(db_column='COD_CT_PROD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUBSTITUICAO_TRIBUTARIA'


class SuperCategoria(models.Model):
    cod_supercat = models.BigIntegerField(db_column='Cod_SuperCat', primary_key=True)  # Field name made lowercase.
    desc_supercat = models.CharField(db_column='Desc_SuperCat', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUPER_CATEGORIA'


class Tabelaprodutos(models.Model):
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    cod_ref = models.IntegerField(db_column='COD_REF', blank=True, null=True)  # Field name made lowercase.
    status_mov = models.CharField(db_column='STATUS_MOV', max_length=1, blank=True, null=True)  # Field name made lowercase.
    data_mov = models.DateTimeField(db_column='DATA_MOV', blank=True, null=True)  # Field name made lowercase.
    qtde_mov = models.IntegerField(db_column='QTDE_MOV', blank=True, null=True)  # Field name made lowercase.
    nf_mov = models.CharField(db_column='NF_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    saldoacum_mov = models.FloatField(db_column='SALDOACUM_MOV', blank=True, null=True)  # Field name made lowercase.
    func_mov = models.CharField(db_column='FUNC_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    maq_mov = models.CharField(db_column='MAQ_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usu_mov = models.CharField(db_column='USU_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.
    resp_mov = models.CharField(db_column='RESP_MOV', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABELAPRODUTOS'


class TipoEnvioEmail(models.Model):
    cod_tip = models.BigIntegerField(blank=True, null=True)
    desc_tip = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TIPO_ENVIO_EMAIL'


class TipoEnvioSkype(models.Model):
    cod_tip = models.BigIntegerField(db_column='COD_TIP', blank=True, null=True)  # Field name made lowercase.
    desc_tip = models.CharField(db_column='DESC_TIP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_ENVIO_SKYPE'


class TipoEnvioTorpedo(models.Model):
    cod_tip = models.BigIntegerField(db_column='COD_TIP', blank=True, null=True)  # Field name made lowercase.
    desc_tip = models.CharField(db_column='DESC_TIP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_ENVIO_TORPEDO'


class TipoPagto(models.Model):
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO', primary_key=True)  # Field name made lowercase.
    desc_pagto = models.CharField(db_column='DESC_PAGTO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    conf_pagto = models.BooleanField(db_column='CONF_PAGTO')  # Field name made lowercase.
    soavista_pagto = models.BooleanField(db_column='SOAVISTA_PAGTO')  # Field name made lowercase.
    naoavista_pagto = models.BooleanField(db_column='NAOAVISTA_PAGTO')  # Field name made lowercase.
    socnf_pagto = models.BooleanField(db_column='SOCNF_PAGTO')  # Field name made lowercase.
    cod_banco = models.BigIntegerField(db_column='COD_BANCO', blank=True, null=True)  # Field name made lowercase.
    disp_vend = models.NullBooleanField(db_column='DISP_VEND')  # Field name made lowercase.
    disp_comp = models.NullBooleanField(db_column='DISP_COMP')  # Field name made lowercase.
    paga_aqui = models.NullBooleanField(db_column='PAGA_AQUI')  # Field name made lowercase.
    valmin_pagto = models.DecimalField(db_column='VALMIN_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_PAGTO'


class Torpedos(models.Model):
    data_torp = models.DateTimeField(db_column='DATA_TORP')  # Field name made lowercase.
    ip_remetente = models.CharField(db_column='IP_REMETENTE', max_length=13)  # Field name made lowercase.
    ip_destino = models.CharField(db_column='IP_DESTINO', max_length=13)  # Field name made lowercase.
    apel_remetente = models.CharField(db_column='APEL_REMETENTE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apel_destino = models.CharField(db_column='APEL_DESTINO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    msg_torp = models.TextField(db_column='MSG_TORP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    recebeu_msg = models.NullBooleanField(db_column='RECEBEU_MSG')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TORPEDOS'
        unique_together = (('data_torp', 'ip_remetente', 'ip_destino'),)


class Transferencia(models.Model):
    cod_transf = models.BigIntegerField(db_column='COD_TRANSF', blank=True, null=True)  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD', blank=True, null=True)  # Field name made lowercase.
    origem_transf = models.CharField(db_column='ORIGEM_TRANSF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    destino_transf = models.CharField(db_column='DESTINO_TRANSF', max_length=1, blank=True, null=True)  # Field name made lowercase.
    qtde_transf = models.BigIntegerField(db_column='QTDE_TRANSF', blank=True, null=True)  # Field name made lowercase.
    user_transf = models.CharField(db_column='USER_TRANSF', max_length=30, blank=True, null=True)  # Field name made lowercase.
    data_transf = models.DateTimeField(db_column='DATA_TRANSF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSFERENCIA'


class Trocas(models.Model):
    cod_os = models.ForeignKey(Os, models.DO_NOTHING, db_column='COD_OS', primary_key=True)  # Field name made lowercase.
    grav_trc = models.CharField(db_column='GRAV_TRC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    veloc_trc = models.CharField(db_column='VELOC_TRC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    soft_trc = models.CharField(db_column='SOFT_TRC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    vers_trc = models.CharField(db_column='VERS_TRC', max_length=20, blank=True, null=True)  # Field name made lowercase.
    obs_trc = models.TextField(db_column='OBS_TRC', blank=True, null=True)  # Field name made lowercase.
    autoriza_trc = models.BooleanField(db_column='AUTORIZA_TRC')  # Field name made lowercase.
    voltouetq_trc = models.BooleanField(db_column='VOLTOUETQ_TRC')  # Field name made lowercase.
    nfdevol_trc = models.CharField(db_column='NFDEVOL_TRC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    criou_orca = models.NullBooleanField(db_column='CRIOU_ORCA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TROCAS'


class TrocasAndamento(models.Model):
    cod_os = models.BigIntegerField(db_column='COD_OS', blank=True, null=True)  # Field name made lowercase.
    operacao = models.CharField(db_column='OPERACAO', max_length=40, blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=30, blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TROCAS_ANDAMENTO'


class Usuarios(models.Model):
    nome_user = models.CharField(db_column='NOME_USER', primary_key=True, max_length=30)  # Field name made lowercase.
    senha_user = models.CharField(db_column='SENHA_USER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cod_niv = models.ForeignKey(Niveis, models.DO_NOTHING, db_column='COD_NIV')  # Field name made lowercase.
    ip_host = models.CharField(db_column='IP_HOST', max_length=13, blank=True, null=True)  # Field name made lowercase.
    apelido_user = models.CharField(db_column='APELIDO_USER', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cod_grupo = models.BigIntegerField(db_column='COD_GRUPO', blank=True, null=True)  # Field name made lowercase.
    apelido_skype = models.CharField(db_column='APELIDO_SKYPE', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USUARIOS'


class Campanhas(models.Model):
    campanha1 = models.IntegerField(blank=True, null=True)
    campanha2 = models.IntegerField(blank=True, null=True)
    campanha3 = models.IntegerField(blank=True, null=True)
    campanha4 = models.IntegerField(blank=True, null=True)
    campanha5 = models.IntegerField(blank=True, null=True)
    campanha6 = models.IntegerField(blank=True, null=True)
    campanha7 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campanhas'


class Clinicas(models.Model):
    cod_cli = models.FloatField(blank=True, null=True)
    nome = models.CharField(db_column='NOME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailgeral = models.CharField(db_column='EMAILGERAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailadm = models.CharField(db_column='EMAILADM', max_length=255, blank=True, null=True)  # Field name made lowercase.
    emailcompras = models.CharField(db_column='EMAILCOMPRAS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel_correto = models.CharField(max_length=255, blank=True, null=True)
    fax_correto = models.CharField(db_column='FAX_CORRETO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cep_trat = models.CharField(db_column='CEP_trat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    administrador = models.CharField(db_column='ADMINISTRADOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clinicas'



class CmpNfe(models.Model):
    cod_cmp = models.BigIntegerField(db_column='Cod_Cmp')  # Field name made lowercase.
    cod_nf_entrada = models.BigIntegerField(db_column='Cod_NF_Entrada')  # Field name made lowercase.
    ativ_cmp_nf = models.BooleanField(db_column='Ativ_Cmp_NF')  # Field name made lowercase.
    empresa_cmp_nf = models.CharField(db_column='Empresa_CMP_NF', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cmp_nfe'


class CmpNfeServ(models.Model):
    cod_cmp_serv = models.BigIntegerField(db_column='Cod_Cmp_Serv')  # Field name made lowercase.
    cod_nf_entrada = models.BigIntegerField(db_column='Cod_NF_Entrada')  # Field name made lowercase.
    ativ_cmp_nf = models.BooleanField(db_column='Ativ_Cmp_NF')  # Field name made lowercase.
    empresa_cmp_nf = models.CharField(db_column='Empresa_CMP_NF', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cmp_nfe_SERV'


class Consultaprod(models.Model):
    cod_prod = models.BigIntegerField()
    data_mov = models.DateTimeField(blank=True, null=True)
    qtde_mov = models.IntegerField(blank=True, null=True)
    desc_prod = models.CharField(max_length=200, blank=True, null=True)
    valor = models.CharField(max_length=8000, blank=True, null=True)
    cod_ref = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consultaprod'


class ContatoCli(models.Model):
    cod_cli = models.BigIntegerField(db_column='COD_CLI')  # Field name made lowercase.
    cod_conta = models.BigIntegerField(db_column='COD_CONTA')  # Field name made lowercase.
    nome_conta = models.CharField(db_column='NOME_CONTA', max_length=40, blank=True, null=True)  # Field name made lowercase.
    email_conta = models.CharField(db_column='EMAIL_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email2_conta = models.CharField(db_column='EMAIL2_CONTA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddd_conta = models.CharField(db_column='DDD_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel_conta = models.CharField(db_column='TEL_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal_conta = models.CharField(db_column='RAMAL_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cargo_conta = models.CharField(db_column='CARGO_CONTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    departamento_conta = models.CharField(db_column='DEPARTAMENTO_CONTA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    receber_email = models.NullBooleanField(db_column='RECEBER_EMAIL')  # Field name made lowercase.
    dddcel_conta = models.CharField(db_column='DDDCEL_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cel_conta = models.CharField(db_column='CEL_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd2_conta = models.CharField(db_column='DDD2_CONTA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_conta = models.CharField(db_column='TEL2_CONTA', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ramal2_conta = models.CharField(db_column='RAMAL2_CONTA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    niver_conta = models.CharField(db_column='NIVER_CONTA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    ativo_conta = models.NullBooleanField(db_column='ATIVO_CONTA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contato_cli'


class Dipj(models.Model):
    cnpj_cli = models.CharField(max_length=18, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dipj'


class EmailInativo(models.Model):
    cod_cli = models.IntegerField(blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'email_inativo'


class ItmNfeEntrada(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_prod = models.BigIntegerField(db_column='COD_PROD')  # Field name made lowercase.
    cod_serv = models.BigIntegerField(db_column='COD_SERV')  # Field name made lowercase.
    qtde_nf_entrada = models.IntegerField(db_column='QTDE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    val_nf_entrada = models.DecimalField(db_column='VAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_nf_entrada = models.DecimalField(db_column='FRETE_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    desconto_nf_entrada = models.DecimalField(db_column='DESCONTO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    st_nf_entrada = models.DecimalField(db_column='ST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    basest_nf_entrada = models.DecimalField(db_column='BASEST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ipi_nf_entrada = models.FloatField(db_column='IPI_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    valoripi_nf_entrada = models.DecimalField(db_column='VALORIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icms_nf_entrada = models.FloatField(db_column='ICMS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cfop_nf_entrada = models.CharField(db_column='CFOP_NF_ENTRADA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sittribut_nf_entrada = models.CharField(db_column='SITTRIBUT_NF_ENTRADA', max_length=3, blank=True, null=True)  # Field name made lowercase.
    pis_nf_entrada = models.FloatField(db_column='PIS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cofins_nf_entrada = models.FloatField(db_column='COFINS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    iss_nf_entrada = models.FloatField(db_column='ISS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    base_ipi = models.DecimalField(db_column='BASE_IPI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valor_nf_prod = models.DecimalField(db_column='VALOR_NF_PROD', max_digits=20, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    base_icms = models.DecimalField(db_column='BASE_ICMS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itm_nfe_entrada'


class ItmNfeEntradaPagto(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    cod_parc = models.IntegerField(db_column='COD_PARC')  # Field name made lowercase.
    val_parc = models.DecimalField(db_column='VAL_PARC', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.IntegerField(db_column='TIPO_PAGTO', blank=True, null=True)  # Field name made lowercase.
    forma_pagto = models.IntegerField(db_column='FORMA_PAGTO', blank=True, null=True)  # Field name made lowercase.
    venc_parc = models.DateTimeField(db_column='VENC_PARC', blank=True, null=True)  # Field name made lowercase.
    pagto_cmp_nf = models.NullBooleanField(db_column='PAGTO_CMP_NF')  # Field name made lowercase.
    real_pagto = models.DecimalField(db_column='REAL_PAGTO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    quit_nf = models.NullBooleanField(db_column='QUIT_NF')  # Field name made lowercase.
    quemquit_nf = models.CharField(db_column='QUEMQUIT_NF', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dataquit_nf = models.DateTimeField(db_column='DATAQUIT_NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itm_nfe_entrada_PAGTO'



class LogRemessa(models.Model):
    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA')  # Field name made lowercase.
    data_remessa = models.DateTimeField(db_column='DATA_REMESSA', blank=True, null=True)  # Field name made lowercase.
    quem_remessa = models.CharField(db_column='QUEM_REMESSA', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_remessa'


class NfeEntradaData(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    numdoc_nf_entrada = models.CharField(db_column='NUMDOC_NF_ENTRADA', max_length=20)  # Field name made lowercase.
    cod_cmp = models.BigIntegerField(db_column='COD_CMP', blank=True, null=True)  # Field name made lowercase.
    modelo_nf_entrada = models.IntegerField(db_column='MODELO_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    serie_nf_entrada = models.IntegerField(db_column='SERIE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.BigIntegerField(db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    nome_forn = models.CharField(db_column='NOME_FORN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_emiss = models.DateTimeField(db_column='DATA_EMISS', blank=True, null=True)  # Field name made lowercase.
    cnpj_nf_entrada = models.CharField(db_column='CNPJ_NF_ENTRADA', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_nf_entrada = models.CharField(db_column='IE_NF_ENTRADA', max_length=19, blank=True, null=True)  # Field name made lowercase.
    uf_nf_entrada = models.CharField(db_column='UF_NF_ENTRADA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valicms_nf_entrada = models.DecimalField(db_column='VALICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valiss_nf_entrada = models.DecimalField(db_column='VALISS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valipi_nf_entrada = models.DecimalField(db_column='VALIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valenvio_nf_entrada = models.DecimalField(db_column='VALENVIO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bcicmsst_nf_entrada = models.DecimalField(db_column='BCICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valtotal_nf_entrada = models.DecimalField(db_column='VALTOTAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valprod_nf_entrada = models.DecimalField(db_column='VALPROD_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valserv_nf_entrada = models.DecimalField(db_column='VALSERV_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icmsst_nf_entrada = models.DecimalField(db_column='ICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    entrega_nf_entrada = models.CharField(db_column='ENTREGA_NF_ENTRADA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pagafrete_nf_entrada = models.CharField(db_column='PAGAFRETE_NF_ENTRADA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    obs_nf_entrada = models.TextField(db_column='OBS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    baselegal_nf_entrada = models.TextField(db_column='BASELEGAL_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    chave_nf_entrada = models.TextField(db_column='CHAVE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    data_entrada = models.DateTimeField(db_column='DATA_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.CharField(db_column='TIPO_PAGTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    base_icms_nf_entrada = models.DecimalField(db_column='BASE_ICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_ENTRADA_DATA'


class NfeEntradaMidia(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    numdoc_nf_entrada = models.CharField(db_column='NUMDOC_NF_ENTRADA', max_length=20)  # Field name made lowercase.
    cod_cmp = models.BigIntegerField(db_column='COD_CMP', blank=True, null=True)  # Field name made lowercase.
    modelo_nf_entrada = models.IntegerField(db_column='MODELO_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    serie_nf_entrada = models.IntegerField(db_column='SERIE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.BigIntegerField(db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    nome_forn = models.CharField(db_column='NOME_FORN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_emiss = models.DateTimeField(db_column='DATA_EMISS', blank=True, null=True)  # Field name made lowercase.
    cnpj_nf_entrada = models.CharField(db_column='CNPJ_NF_ENTRADA', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_nf_entrada = models.CharField(db_column='IE_NF_ENTRADA', max_length=19, blank=True, null=True)  # Field name made lowercase.
    uf_nf_entrada = models.CharField(db_column='UF_NF_ENTRADA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valicms_nf_entrada = models.DecimalField(db_column='VALICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valiss_nf_entrada = models.DecimalField(db_column='VALISS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valipi_nf_entrada = models.DecimalField(db_column='VALIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valenvio_nf_entrada = models.DecimalField(db_column='VALENVIO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bcicmsst_nf_entrada = models.DecimalField(db_column='BCICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valtotal_nf_entrada = models.DecimalField(db_column='VALTOTAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valprod_nf_entrada = models.DecimalField(db_column='VALPROD_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valserv_nf_entrada = models.DecimalField(db_column='VALSERV_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icmsst_nf_entrada = models.DecimalField(db_column='ICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    entrega_nf_entrada = models.CharField(db_column='ENTREGA_NF_ENTRADA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pagafrete_nf_entrada = models.CharField(db_column='PAGAFRETE_NF_ENTRADA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    obs_nf_entrada = models.TextField(db_column='OBS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    baselegal_nf_entrada = models.TextField(db_column='BASELEGAL_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    chave_nf_entrada = models.TextField(db_column='CHAVE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    data_entrada = models.DateTimeField(db_column='DATA_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.CharField(db_column='TIPO_PAGTO', max_length=10, blank=True, null=True)  # Field name made lowercase.
    base_icms_nf_entrada = models.DecimalField(db_column='BASE_ICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_ENTRADA_midia'


class NfeEntrada(models.Model):
    cod_nf_entrada = models.BigIntegerField(db_column='COD_NF_ENTRADA')  # Field name made lowercase.
    numdoc_nf_entrada = models.CharField(db_column='NUMDOC_NF_ENTRADA', max_length=20)  # Field name made lowercase.
    cod_cmp = models.BigIntegerField(db_column='COD_CMP', blank=True, null=True)  # Field name made lowercase.
    modelo_nf_entrada = models.IntegerField(db_column='MODELO_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    serie_nf_entrada = models.IntegerField(db_column='SERIE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_nat = models.CharField(db_column='COD_NAT', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cod_forn = models.BigIntegerField(db_column='COD_FORN', blank=True, null=True)  # Field name made lowercase.
    nome_forn = models.CharField(db_column='NOME_FORN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    data_emiss = models.DateTimeField(db_column='DATA_EMISS', blank=True, null=True)  # Field name made lowercase.
    cnpj_nf_entrada = models.CharField(db_column='CNPJ_NF_ENTRADA', max_length=18, blank=True, null=True)  # Field name made lowercase.
    ie_nf_entrada = models.CharField(db_column='IE_NF_ENTRADA', max_length=19, blank=True, null=True)  # Field name made lowercase.
    uf_nf_entrada = models.CharField(db_column='UF_NF_ENTRADA', max_length=2, blank=True, null=True)  # Field name made lowercase.
    valicms_nf_entrada = models.DecimalField(db_column='VALICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valiss_nf_entrada = models.DecimalField(db_column='VALISS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valipi_nf_entrada = models.DecimalField(db_column='VALIPI_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valenvio_nf_entrada = models.DecimalField(db_column='VALENVIO_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bcicmsst_nf_entrada = models.DecimalField(db_column='BCICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valtotal_nf_entrada = models.DecimalField(db_column='VALTOTAL_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valprod_nf_entrada = models.DecimalField(db_column='VALPROD_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    valserv_nf_entrada = models.DecimalField(db_column='VALSERV_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    icmsst_nf_entrada = models.DecimalField(db_column='ICMSST_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    entrega_nf_entrada = models.CharField(db_column='ENTREGA_NF_ENTRADA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pagafrete_nf_entrada = models.CharField(db_column='PAGAFRETE_NF_ENTRADA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    obs_nf_entrada = models.TextField(db_column='OBS_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    baselegal_nf_entrada = models.TextField(db_column='BASELEGAL_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    chave_nf_entrada = models.TextField(db_column='CHAVE_NF_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    cod_mod = models.CharField(db_column='COD_MOD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cod_sit = models.CharField(db_column='COD_SIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    data_entrada = models.DateTimeField(db_column='DATA_ENTRADA', blank=True, null=True)  # Field name made lowercase.
    tipo_pagto = models.CharField(db_column='TIPO_PAGTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    base_icms_nf_entrada = models.DecimalField(db_column='BASE_ICMS_NF_ENTRADA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nfe_entrada'


class Tblaliqst(models.Model):
    id = models.AutoField(db_column='ID')  # Field name made lowercase.
    ncm = models.ForeignKey('Tblncm', models.DO_NOTHING, db_column='NCM', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mva_ajustado = models.CharField(db_column='MVA_AJUSTADO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mva_imp = models.CharField(db_column='MVA_IMP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mva_original = models.CharField(db_column='MVA_ORIGINAL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    icms_intra_r = models.CharField(db_column='ICMS_INTRA_R', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblAliqSt'


class Tblicms(models.Model):
    estado = models.CharField(db_column='ESTADO', primary_key=True, max_length=50)  # Field name made lowercase.
    icms = models.CharField(db_column='ICMS', max_length=50)  # Field name made lowercase.
    icms_st = models.CharField(db_column='ICMS_ST', max_length=50)  # Field name made lowercase.
    icms_imp = models.CharField(db_column='ICMS_IMP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fcp = models.CharField(db_column='FCP', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblIcms'


class Tblncm(models.Model):
    ncm = models.CharField(db_column='NCM', primary_key=True, max_length=50)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblNcm'


class TempLojaPedido(models.Model):
    idpedido = models.BigIntegerField()
    data1_os = models.DateTimeField(db_column='DATA1_OS', blank=True, null=True)  # Field name made lowercase.
    cod_pagto = models.BigIntegerField(db_column='COD_PAGTO', blank=True, null=True)  # Field name made lowercase.
    cod_ent = models.BigIntegerField(db_column='COD_ENT')  # Field name made lowercase.
    tot_os = models.DecimalField(db_column='TOT_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    frete_os = models.DecimalField(db_column='FRETE_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pesoprod_os = models.FloatField(db_column='PESOPROD_OS', blank=True, null=True)  # Field name made lowercase.
    subst_tributaria = models.DecimalField(db_column='SUBST_TRIBUTARIA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    descsuframa_os = models.DecimalField(db_column='DESCSUFRAMA_OS', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=30, blank=True, null=True)
    bairro = models.CharField(max_length=20, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    nome_trans_ent = models.CharField(db_column='NOME_TRANS_ENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ddd_trans_ent = models.CharField(db_column='DDD_TRANS_ENT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    telefone_trans_ent = models.CharField(db_column='TELEFONE_TRANS_ENT', max_length=9, blank=True, null=True)  # Field name made lowercase.
    pagcomp1 = models.CharField(max_length=2550, blank=True, null=True)
    email_cli = models.CharField(db_column='EMAIL_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nome_cli = models.CharField(db_column='NOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.
    pes_cli = models.CharField(db_column='PES_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    contato_cli = models.CharField(db_column='CONTATO_CLI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    end_cli = models.CharField(db_column='END_CLI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    num_cli = models.CharField(db_column='NUM_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bair_cli = models.CharField(db_column='BAIR_CLI', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cid_cli = models.CharField(db_column='CID_CLI', max_length=30, blank=True, null=True)  # Field name made lowercase.
    est_cli = models.CharField(db_column='EST_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cep_cli = models.CharField(db_column='CEP_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    cpf_cli = models.CharField(db_column='CPF_CLI', max_length=14, blank=True, null=True)  # Field name made lowercase.
    cnpj_cli = models.CharField(db_column='CNPJ_CLI', max_length=18, blank=True, null=True)  # Field name made lowercase.
    rg_cli = models.CharField(db_column='RG_CLI', max_length=13, blank=True, null=True)  # Field name made lowercase.
    ie_cli = models.CharField(db_column='IE_CLI', max_length=19, blank=True, null=True)  # Field name made lowercase.
    ddd1_cli = models.CharField(db_column='DDD1_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel1_cli = models.CharField(db_column='TEL1_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ddd2_cli = models.CharField(db_column='DDD2_CLI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tel2_cli = models.CharField(db_column='TEL2_CLI', max_length=9, blank=True, null=True)  # Field name made lowercase.
    suframa_cli = models.CharField(db_column='SUFRAMA_CLI', max_length=12, blank=True, null=True)  # Field name made lowercase.
    revenda_cli = models.CharField(db_column='REVENDA_CLI', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cod_divulg = models.BigIntegerField(db_column='COD_DIVULG', blank=True, null=True)  # Field name made lowercase.
    export = models.NullBooleanField()
    num_cartao = models.CharField(max_length=16, blank=True, null=True)
    cod_seguranca = models.CharField(max_length=3, blank=True, null=True)
    cod_legivel = models.NullBooleanField()
    data_validade = models.DateTimeField(blank=True, null=True)
    nome_impresso = models.CharField(max_length=50, blank=True, null=True)
    sobrenome_cli = models.CharField(db_column='SOBRENOME_CLI', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temp_loja_pedido'


