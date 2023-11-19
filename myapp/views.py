from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hola(request):
    return HttpResponse("Hello Word")

def AcercaDe(request):
    return HttpResponse('Bienvenido a about')