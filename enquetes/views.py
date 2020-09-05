from django.shortcuts import render
from enquetes.models import Enquete

def index(request):
    return render(request, 'bemvindo.html')

def exibir(request, enquete_id):
    enquete = Enquete()

    if enquete_id == 1:
        enquete = Enquete("", "Você escuta PodCast ?", "17/08/2020")
    
    if enquete_id == 2:
        enquete = Enquete("", "Qual é o seu PodCast preferido?", "18/08/2020")
    
    if enquete_id == 3:
        enquete = Enquete("", "Caso tenha respondido a pergunta anterior, escreva qual episódio do PodCast mais te marcou.", "19/08/2020")
    
    return render(request, 'enquete.html', {"enquete": enquete})

# Create your views here.
