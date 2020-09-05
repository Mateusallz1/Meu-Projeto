from django.db import models

class Enquete(models.Model):
    '''
        def __init__(self, id = 0, texto= '', data= ''):
        self.id = id
        self.texto = texto
        self.data = data *GAMBIARRA*
    '''
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateField()

# Create your models here.
