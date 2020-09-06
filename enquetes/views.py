from django.shortcuts import render
from enquetes.models import Enquete

def index(request):
    return render(request, 'bemvindo.html')

def exibir(request, enquete_id):
    enquete = Enquete()
    enquete = Enquete.objects.get(id=enquete_id)
    return render(request,'enquete.html',{"enquete":enquete})
    
# Create your views here.
