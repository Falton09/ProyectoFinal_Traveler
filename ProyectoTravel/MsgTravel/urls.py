from django.urls import path

from MsgTravel.views import *

urlpatterns = [
    path('elegir_reseptor/', elegir_reseptor, name= 'MsgTravelElegirReseptor'),
    path('mensaje/<str:username>', mensaje, name= 'MsgTravelMensaje'),
    path('mis_conversaciones/', mis_conversaciones, name= 'MsgTravelMisConversaciones'),



]
