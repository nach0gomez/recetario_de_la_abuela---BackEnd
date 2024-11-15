from django.shortcuts import render
from .models import Receta

# Create your views here.
def Login(request):
    return render(request, 'login.html')

def getReceta(request):
    #return render(request, 'eventos.html', {'eventos': eventos})
    getrecetas = Receta.objects.all()
    #eventos = Receta.objects.filter(user=request.user, estado = 'Activo')
    #return request
    return render(request, 'get-recetas.html', {'getrecetas': getrecetas})
