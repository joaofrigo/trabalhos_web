from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, '2K_inspired.html') # retorna um html

def exemplo_view(request):
    return HttpResponse("Essa é a view de exemplo") # retorna uma resposta em html
