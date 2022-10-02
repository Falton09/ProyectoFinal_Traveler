from django.urls import path

from MsgTravel.views import *

urlpatterns = [
    path('elegir_reseptor/', elegir_reseptor, name= 'MsgTravelElegirReseptor'),
    path('mensaje/<str:username>/', hilos, name= 'MsgTravelHilos'),
    path('enviado/<str:reseptor>/', en_conversacion, name= 'MsgTravelEnConversacion'),

]
