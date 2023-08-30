from django.contrib.auth.models import User
from django.db import models

OPCOES_CAMBIO = [
    ('MANUAL', 'MANUAL'),
    ('AUTOMATIZADO', 'AUTOMATIZADO'),
    ('AUTOMÁTICO', 'AUTOMÁTICO'),
    ('CVT', 'CVT'),
]

OPCOES_VEICULO = [
    ('MOTO', 'Moto'),
    ('CARRO', 'Carro'),
    ('VANS', 'Vans'),
    ('CAMINHOES', 'Caminhoes'),
]

OPCOES_COMBUSTIVEL = [
    ('GASOLINA','GASOLINA'),
    ('ÁLCOOL','ÁLCOOL'),
    ('DIESEL','DIESEL'),
    ('ELÉTRICO','ELÉTRICO'),
    ('HÍBRIDO','HÍBRIDO'),
    ('GASOLINA E ÁLCOOL','GASOLINA E ÁLCOOL'),
    ('GNV', 'GNV'),
]

def upload_too(instance, filename):
    marca = instance.marca
    return f'logos/{marca}.png'

def upload_to(instance, filename):
    veiculo_id = instance.veiculo.id
    numero = instance.veiculo.fotos.count() + 1
    nome, ext = filename.split('.')
    nome_arquivo = f'{veiculo_id}_{nome}_{numero}.{ext}'
    return f'foto/{nome_arquivo}'

class Marca(models.Model):
    marca = models.CharField(max_length=20, null=False, blank= False)
    logo = models.ImageField(upload_to='logos', default='', blank=True)
    tipo = models.CharField(max_length=30, choices=OPCOES_VEICULO, default='')

    def __str__(self):
        return f'{self.marca}'

class Veiculo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', default=None)
    nome = models.CharField(max_length=20, null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='marcas', default=None)
    ano = models.CharField(max_length=12, null=False, blank=False)
    km = models.FloatField(null=False, blank=False)
    valor = models.FloatField(null=False, blank=False)
    tipo = models.CharField(max_length=30, choices=OPCOES_VEICULO, default='')
    motor = models.CharField(max_length=20, null=False, blank=False)
    cor = models.CharField(max_length=20, null=False, blank=True)
    câmbio = models.CharField(max_length=100, choices=OPCOES_CAMBIO, default='')
    combustivel = models.CharField(max_length=30, choices=OPCOES_COMBUSTIVEL, default='')
    legenda = models.TextField(max_length=80, null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    veiculo = models.ForeignKey(Veiculo, related_name='fotos', on_delete=models.CASCADE, default=1)
    posicao = models.CharField(max_length=3, default='')
    imagem = models.ImageField(upload_to='images', default=None)


    def __str__(self):
        return f'Foto {self.pk} - Veiculo {self.veiculo.nome}'

