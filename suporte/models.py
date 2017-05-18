from django.db import models

# Create your models here.

class PerennityLicense(models.Model):
    TRIAL = 0
    DEMO = 1
    FULL = 2
    STATUS_LICENSE = (
        (TRIAL, 'Amostra'),
        (DEMO, 'Demonstração'),
        (FULL, 'Licenciado'),
    )

    tecnico = models.ForeignKey('auth.User', related_name='tecnicos')
    cliente = models.CharField('Cliente', max_length=250)
    mac_address = models.CharField('MacAddress', max_length=250)
    serial = models.CharField('SN', max_length=100, unique=True, null=True, blank=True)
    installed = models.DateField('Instalado', null=True, blank=True)
    valid = models.DateField('Valido', null=True, blank=True)
    key = models.TextField('Chave', null=True, blank=True)
    active = models.NullBooleanField('Licença Ativa', default=True)
    tipo_license = models.PositiveIntegerField('Status', choices=STATUS_LICENSE, default=TRIAL)

    nao_enviar_aviso =  models.NullBooleanField(default=False)
    data_ultimo_aviso =  models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-valid']

    def __str__(self):
        return '%s | %s' % (self.cliente, self.mac_address)

    @property
    def tecnico_name(self):
        names = (self.tecnico.first_name, self.tecnico.last_name)
        return ' '.join(names) or None
