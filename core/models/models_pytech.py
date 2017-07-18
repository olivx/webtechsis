from django.contrib.auth.models import User
from django.db import models



class ProdutoPytech(models.Model):
    cliente = models.ForeignKey('ClientePytech', null=True, blank=True, related_name='produtos')
    desc = models.CharField('DESC', max_length=100)
    ativo = models.NullBooleanField(default=True)
    sn = models.CharField('SN', max_length=18)

    def __str__(self):
        return '{} | {}'.format(self.desc, self.sn)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Pytech Produto '
        verbose_name_plural = 'Pytech Produtos'


class GrupoClientePytech(models.Model):
    name = models.CharField('Nome do Grupo', max_length=100)


class ClientePytech(models.Model):
    HOSPITAL = 1
    CLINICA = 2
    GRAFICA = 3
    IGREJA = 4
    INDUSTRIA = 5
    SEGURANÇA = 6
    OUTROS = 7

    TIPO_CLIENTE = (
        (HOSPITAL, 'Hospital'),
        (CLINICA, 'Clinica Medica'),
        (GRAFICA, 'Graficas'),
        (IGREJA, 'Igrejas'),
        (INDUSTRIA, 'Industrias'),
        (SEGURANÇA, 'Epresas de Seguranças'),
        (OUTROS, 'Outros'),
    )

    id_reff = models.PositiveIntegerField('ID Sistech')
    name = models.CharField('Razão Social', max_length=255)
    nick_name = models.CharField('Apelido', max_length=200, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    active = models.NullBooleanField(default=False)
    tipo = models.PositiveIntegerField('Ramo', default=HOSPITAL, choices=TIPO_CLIENTE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-created']

    def __str__(self):
        return '{} ({})'.format(self.name, self.nick_name)



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