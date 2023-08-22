from django.db import models
from django.utils import timezone

# Create your models here.

class MeusDados(models.Model):
    nome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30, default=None)
    data_nascimento = models.DateField()
    celular_whatsapp = models.CharField(max_length=15)
    email = models.EmailField()
    habilitacao = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class MeuPortifolio(models.Model):
    projeto = models.CharField(max_length=50)
    descricao_projeto = models.TextField(max_length=10000)
    data_criacao = models.DateTimeField(default=timezone.now)
    download = models.FileField(upload_to='media/projetos')
    imagem = models.ImageField(upload_to='media/imagens')

    def __str__(self):
        return self.projeto

class Formacao(models.Model):
    nome = models.ForeignKey("MeusDados", related_name='formacao',on_delete=models.CASCADE)
    formacao = models.CharField(max_length=50)
    descricao = models.TextField(max_length=10000)

    def __str__(self):
        return self.formacao

class Experiencias(models.Model):
    nome = models.ForeignKey("MeusDados", related_name='experiencia',on_delete=models.CASCADE)
    experiencia = models.CharField(max_length=50)
    descricao = models.TextField(max_length=10000)

    def __str__(self):
        return self.experiencia

class Cursos(models.Model):
    nome = models.ForeignKey("MeusDados", related_name='curso', on_delete=models.CASCADE)
    curso = models.CharField(max_length=50)
    descricao = models.TextField(max_length=10000)

    def __str__(self):
        return self.curso

class Infos(models.Model):
    nome = models.ForeignKey("MeusDados", related_name='info', on_delete=models.CASCADE)
    info = models.CharField(max_length=50)
    descricao = models.TextField(max_length=10000)
    nivel = models.DecimalField(max_digits=4, decimal_places=2, default=10)

    def __str__(self):
        return self.info

class MinhaHistoria(models.Model):
    nome = models.ForeignKey("MeusDados", related_name='minhahistoria', on_delete=models.CASCADE)
    historia = models.TextField(max_length=1000)
    data_atualizacao = models.DateTimeField(default=timezone.now)
