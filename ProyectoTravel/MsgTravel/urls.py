from django.urls import path

from MsgTravel.views import *

urlpatterns = [
    path('elegir_reseptor/', elegir_reseptor, name= 'MsgTravelElegirReseptor'),
    path('mensaje/<str:username>/', mensaje, name= 'MsgTravelMensaje'),
    path('enviado/<str:reseptor>/', en_conversacion, name= 'MsgTravelEnConversacion'),
    # path('resivido/<str:emisor>', en_conversacion_emisor, name= 'MsgTravelEnConversacionEmisor'),



]
