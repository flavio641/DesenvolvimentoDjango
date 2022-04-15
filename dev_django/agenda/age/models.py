from pickle import TRUE
from django.db import models

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=TRUE)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)


def __str__(self):
    return self.titulo
