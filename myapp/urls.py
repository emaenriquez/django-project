
from django.urls import path
from . import views

urlpatters = [
    path('',views.hola),
    path('about/',views.AcercaDe)
]