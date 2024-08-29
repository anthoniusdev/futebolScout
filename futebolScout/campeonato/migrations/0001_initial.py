# Generated by Django 5.1 on 2024-08-29 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clube', '__first__'),
        ('federacao', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nameRights', models.CharField(max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('logo_path', models.ImageField(blank=True, null=True, upload_to='imagens/campeonato/')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('clubes', models.ManyToManyField(to='clube.clube')),
                ('federacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='federacao.federacao')),
            ],
        ),
    ]
