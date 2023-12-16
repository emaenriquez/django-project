from django.contrib import admin
from django.urls import path, include
# importamos solo una funcion del archivo
# from myapp.views import hola
#  importamos todo el archivo
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.holaMundo),
    path('about/',views.AcercaDe),
    path('hello/',views.hola)
]
