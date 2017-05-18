# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-18 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170510_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('cod_cat', models.BigIntegerField(db_column='COD_CAT', primary_key=True, serialize=False)),
                ('desc_cat', models.CharField(blank=True, db_column='DESC_CAT', max_length=40, null=True)),
                ('cod_supercat', models.BigIntegerField(blank=True, db_column='COD_SUPERCAT', null=True)),
                ('mostrar_cat', models.CharField(blank=True, db_column='MOSTRAR_CAT', max_length=17, null=True)),
                ('apelido_cat', models.CharField(blank=True, db_column='APELIDO_CAT', max_length=50, null=True)),
            ],
            options={
                'db_table': 'CATEGORIAS',
                'managed': False,
                'verbose_name_plural': 'Categorias',
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('cod_prod', models.BigIntegerField(db_column='COD_PROD', primary_key=True, serialize=False)),
                ('desc_prod', models.CharField(blank=True, db_column='DESC_PROD', max_length=300, null=True)),
                ('min_prod', models.IntegerField(blank=True, db_column='MIN_PROD', null=True)),
                ('saldo_prod', models.BigIntegerField(blank=True, db_column='SALDO_PROD', null=True)),
                ('teorico_prod', models.BigIntegerField(blank=True, db_column='TEORICO_PROD', null=True)),
                ('custoref_prod', models.DecimalField(blank=True, db_column='CUSTOREF_PROD', decimal_places=4, max_digits=19, null=True)),
                ('custo_prod', models.DecimalField(blank=True, db_column='CUSTO_PROD', decimal_places=4, max_digits=19, null=True)),
            ],
            options={
                'db_table': 'PRODUTOS',
                'managed': False,
                'verbose_name_plural': 'Produtos',
                'verbose_name': 'Produto',
            },
        ),
        migrations.RemoveField(
            model_name='perennitylicense',
            name='tecnico',
        ),
        migrations.DeleteModel(
            name='PerennityLicense',
        ),
    ]
