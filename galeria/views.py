from django.shortcuts import render
from django.http import HttpResponse

# Função principal da aplicação
def index(request):
    return HttpResponse('<h1>Olá mundo!</h1><p>Bem vindo ao espaço</p>')

