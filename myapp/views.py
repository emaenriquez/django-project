from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def holaMundo(request):
    return HttpResponse('hola mundo desde django')

def hola(request, username):
    print(username)
    return HttpResponse("Hello Word")


def AcercaDe(request):
    return HttpResponse('Bienvenido a about')