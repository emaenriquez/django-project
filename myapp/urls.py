
from django.urls import path
from . import views

urlpatters = [
    path('',views.holaMundo),
    path('about/',views.AcercaDe),
    path('hello/<str:username>',views.hola, name="hello")
]