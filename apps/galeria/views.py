from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

# Função principal da aplicação
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galeria/imagem.html', {'fotografia': foto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado!')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/buscar.html', {'cards': fotografias})

