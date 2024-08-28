# Generated by Django 5.1 on 2024-08-28 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('clube', '0002_remove_clube_jogadores'),
        ('federacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clube',
            name='federacao',
        ),
        migrations.AddField(
            model_name='clube',
            name='federacoes',
            field=models.ManyToManyField(blank=True, to='federacao.federacao'),
        ),
        migrations.AlterField(
            model_name='clube',
            name='criado_por',
            field=models.ForeignKey(auto_created=True, blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.pessoa'),
        ),
    ]
