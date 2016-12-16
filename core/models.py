from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in




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



    # macarrao que tinha feito , não é mais necessario
    # def get_tech_user_signal(sender, user, request, **kwargs):
    #     # if not user.is_superuser:
    #     #     test_user = TechDjangoUser.objects.get(django_user=user)
    #     #     tech_user = TechUser.objects.using('techcd').get(username=test_user.tech_user)
    #     #     request.session['tech_user'] = tech_user
    #
    # user_logged_in.connect(get_tech_user_signal)






#








