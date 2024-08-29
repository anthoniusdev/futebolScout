# Generated by Django 5.1 on 2024-08-29 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('clube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentariosJogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_pessoa_jogador', to='accounts.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_jogador', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('altura', models.FloatField()),
                ('melhor_pe', models.CharField(choices=[('Esquerdo', 'Esquerdo'), ('Direito', 'Direito'), ('Ambidestro', 'Ambidestro')], max_length=100)),
                ('foto_path', models.ImageField(blank=True, null=True, upload_to='imagens/jogador/')),
                ('fotoCapa_path', models.ImageField(blank=True, null=True, upload_to='imagens/jogador/')),
                ('nota_media', models.FloatField(default=0.0, editable=False)),
                ('posicao', models.CharField(choices=[('Goleiro', 'Goleiro'), ('Zagueiro', 'Zagueiro'), ('Lateral Esquerdo', 'Lateral Esquerdo'), ('Lateral Direito', 'Lateral Direito'), ('Volante', 'Volante'), ('Meio Campo', 'Meio Campo'), ('Meia atacante', 'Meia atacante'), ('Ponta esquerda', 'Ponta esquerda'), ('Ponta direita', 'Ponta direita'), ('Centroavante', 'Centroavante'), ('Atacante', 'Atacante')], max_length=100)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('clube', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clube.clube')),
                ('comentarios', models.ManyToManyField(blank=True, related_name='jogador_comentarios', through='jogador.ComentariosJogador', to='accounts.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='comentariosjogador',
            name='jogador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_jogador', to='jogador.jogador'),
        ),
    ]
