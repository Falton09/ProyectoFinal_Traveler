from django.urls import path

from AppTravel.views import *

urlpatterns = [
    path('', inicio, name='AppTravelInicio'),
    path('vuelos/',vuelo, name='AppTravelVuelos'),
    path('reservahotel/',reserva_hotel, name='AppTravelReservaHotel'),
    path('busqueda/',busqueda, name='AppTravelBusqueda'),
    

]