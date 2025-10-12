from django.shortcuts import render

# Função principal da aplicação
def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

