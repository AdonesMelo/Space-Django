from django.db import models
from datetime import datetime

class fotografia(models.Model):
    OPCAO_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=150, choices=OPCAO_CATEGORIA, default='')
    decricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d', blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
