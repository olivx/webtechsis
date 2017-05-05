from django.db import models
from django.shortcuts import resolve_url





class BoletoAbstract(models.Model):
    nnum_bol = models.BigIntegerField('CODIGO BOLETO',db_column='NNum_Bol', primary_key=True)  # Field name made lowercase.
    data_bol = models.DateTimeField('DATA EMISSÃO',db_column='Data_Bol', blank=True, null=True)  # Field name made lowercase.
    venc_bol = models.DateTimeField('DATA VENCIMENTO',db_column='Venc_Bol', blank=True, null=True)  # Field name made lowercase.
    numdoc_bol = models.BigIntegerField('NFE ', db_column='NumDoc_Bol', blank=True, null=True)  # Field name made lowercase.
    val_bol = models.CharField('VALOR ', db_column='Val_Bol', max_length=53, blank=True, null=True)  # Field name made lowercase.
    sac_bol = models.CharField('CLIENTE', db_column='Sac_Bol', max_length=30, blank=True, null=True)  # Field name made lowercase.
    end_bol = models.CharField('ENDEREÇO',db_column='End_Bol', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cep_bol = models.CharField('CEP',db_column='Cep_Bol', max_length=10, blank=True, null=True)  # Field name made lowercase.
    bair_bol = models.CharField('BAIRRO' ,db_column='Bair_Bol', max_length=12, blank=True, null=True)  # Field name made lowercase.
    cid_bol = models.CharField('CIDADE',db_column='Cid_Bol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uf_bol = models.CharField('ESTADO',db_column='UF_Bol', max_length=2, blank=True, null=True)  # Field name made lowercase.
    pes_bol = models.CharField('TIPO CLIENTE',db_column='Pes_Bol', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cnpj_bol = models.CharField('CNPJ',db_column='CNPJ_Bol', max_length=14, blank=True, null=True)  # Field name made lowercase.
    env_bol = models.NullBooleanField('ENVIADO',db_column='Env_Bol')  # Field name made lowercase.
    ind_tip_nfe_srv = models.NullBooleanField('SERVIÇO',db_column='IND_TIP_NFE_SRV')  # Field name made lowercase.

    class Meta:
        abstract = True
        verbose_name = 'Boleto'
        verbose_name_plural = 'Boletos'

    def __str__(self):
        return self.sac_bol

class BoletoData(BoletoAbstract):

    def get_absolute_url(self):
        return resolve_url('boletos:boleto_data_detail', nnum_bol=self.nnum_bol)

    class Meta:
        managed = False
        db_table = 'BOLETOS_DATA_NFE'

class BoletoMidia(BoletoAbstract):
    def get_absolute_url(self):
        return resolve_url('boletos:boleto_midia_detail', nnum_bol=self.nnum_bol)

    class Meta:
        managed = False
        db_table = 'BOLETOS_MIDIA_NFE'

class BoletoTech(BoletoAbstract):

    def get_absolute_url(self):
        return resolve_url('boletos:boleto_tech_detail', nnum_bol=self.nnum_bol)

    class Meta:
        managed = False
        db_table = 'BOLETOS_TECHCD_NFE'


class ItmNfeSaidaPagtoAbstract(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Item NFe Saida'
        verbose_name = 'Itens NFe Saida'

        unique_together = ('cod_nf_saida', 'datavencnf_saida_pagto')

    cod_nf_saida = models.BigIntegerField(db_column='COD_NF_SAIDA', primary_key=True)  # Field name made lowercase.
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



    def __str__(self):
        return '{0} - {1} - {2}'.format(str(self.cod_nf_saida), str(self.datavencnf_saida_pagto), str(self.valnf_saida_pagto))




class ItemNfeSaidaPagtoTech(ItmNfeSaidaPagtoAbstract):

    class Meta:
        managed = False
        db_table =  'ITM_NFE_SAIDA_PAGTO'

class ItemNfeSaidaPagtoData(ItmNfeSaidaPagtoAbstract):

    class Meta:
        managed = False
        db_table =  'ITM_NFE_SAIDA_PAGTO_DATA'

class ItemNfeSaidaPagtoMidia(ItmNfeSaidaPagtoAbstract):

    class Meta:
        managed = False
        db_table =  'ITM_NFE_SAIDA_PAGTO_MIDIA'


class ItemNfeSaidaPagtoTechSRV(ItmNfeSaidaPagtoAbstract):
    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_SRV'


class ItemNfeSaidaPagtoDataSRV(ItmNfeSaidaPagtoAbstract):
    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_DATA_SRV'


class ItemNfeSaidaPagtoMidiaSRV(ItmNfeSaidaPagtoAbstract):
    class Meta:
        managed = False
        db_table = 'ITM_NFE_SAIDA_PAGTO_MIDIA_SRV'






