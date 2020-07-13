from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def teste(request) :
    # html = "<html> <head> </head> <body> <h1> OLA MUNDO CRUEL!!! </h1></body> </html>";
    # aux = HttpResponse(html);
    # return aux;
    return render(request, "MeuSite.html");

def teste2(request) :
    # html = "<html> <head> </head> <body> <h1> OLA MUNDO CRUEL!!! </h1></body> </html>";
    # aux = HttpResponse(html);
    # return aux;
    return render(request, "Teste2.html");