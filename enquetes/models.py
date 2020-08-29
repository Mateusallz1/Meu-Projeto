from django.db import models

class Enquete(object):
    def __init__(self, id = 0, texto= '', data= ''):
        self.id = id
        self.texto = texto
        self.data = data

# Create your models here.
