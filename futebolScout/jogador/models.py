from django.db import models
from accounts.models import Pessoa

class Jogador(models.Model):
    POSICAO_CHOICES = [
        ('Goleiro', 'Goleiro'),
        ('Zagueiro', 'Zagueiro'),
        ('Lateral Esquerdo', 'Lateral Esquerdo'),
        ('Lateral Direito', 'Lateral Direito'),
        ('Volante', 'Volante'),
        ('Meio Campo', 'Meio Campo'),
        ('Meia atacante', 'Meia atacante'),
        ('Ponta esquerda', 'Ponta esquerda'),
        ('Ponta direita', 'Ponta direita'),
        ('Centroavante', 'Centroavante'),
        ('Atacante', 'Atacante'),
    ]
    MELHOR_PE_CHOICES = [
        ('Esquerdo', 'Esquerdo'),
        ('Direito', 'Direito'),
        ('Ambidestro', 'Ambidestro'),
    ]

    escolhas_avaliacao = [(i, str(i)) for i in range(11)] 
    nome_jogador = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    descricao = models.TextField() 
    altura = models.FloatField()
    melhor_pe = models.CharField(choices=MELHOR_PE_CHOICES, max_length=100)
    foto_path = models.ImageField(upload_to='jogador/rosto/', null=True, blank=True)
    fotoCapa_path = models.ImageField(upload_to='jogador/capa/', null=True, blank=True)
    nota_media = models.FloatField(default=0.0, editable=False)
    clube = models.ForeignKey('clube.Clube', on_delete=models.SET_NULL, default=None, null=True, blank=True)
    posicao = models.CharField(choices=POSICAO_CHOICES, max_length=100)
    
        
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)