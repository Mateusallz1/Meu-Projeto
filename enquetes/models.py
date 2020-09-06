from django.db import models
from datetime import date

class Enquete(models.Model):
    '''
        def __init__(self, id = 0, texto= '', data= ''):
        self.id = id
        self.texto = texto
        self.data = data *GAMBIARRA*
    '''
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateField(default=date.today().strftime('%Y-%m-%d'))

# Create your models here.
