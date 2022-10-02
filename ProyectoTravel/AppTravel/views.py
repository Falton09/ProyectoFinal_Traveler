from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AppTravel.forms import NuevoVuelo, ReservaHotel
from AppTravel.models import Hotel,Vuelo
from UserTravel.models import Testimonio
from django.contrib.auth.models import User
from django.contrib import messages


#inicio de la pagina, va hacer un login para que la informacion se entrelace
def inicio(request):

    testimonios = Testimonio.objects.all()
    contexto={'testimonios':testimonios}


    return render(request, 'index.html',contexto)

#se crea el formulario de Vuelo del usuario
def vuelo(request):
    
    if request.method == 'POST':
        mi_formulario = NuevoVuelo(request.POST)
        
        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
    
            user = request.user
            try:
                vuelo1 = Vuelo(user=user,destino=data.get('destino'), fecha_salida=data.get('fecha_salida'), fecha_regreso=data.get('fecha_regreso'), num_personas=data.get('num_personas'))
            
                vuelo1.save()
            except:
                messages.error(request, "No Puede Reservar Vuelos sin un Usuario, Por Favor Registrarse o Logearse")

                return redirect('AppTravelInicio')
            

    contexto = {
    'form': NuevoVuelo()
            }


    return render(request, 'AppTravel/vuelos.html',contexto)
                        

#creacion de formulario para la parte de reserva de hotel 
def reserva_hotel(request):

    if request.method == 'POST':
        mi_formulario = ReservaHotel(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            user = request.user
            try:
                hotel1 = Hotel(user=user,nombreH=data.get('nombreH'), num_personas=data.get('num_personas'), dia_entrada=data.get('dia_entrada'), dia_salida=data.get('dia_salida'))
                hotel1.save()
            except:
                messages.error(request, "No Puede Reservar Hotel sin un Usuario, Por Favor Registrarse o Logearse")

                return redirect('AppTravelInicio')
   
    contexto = {
        'form': ReservaHotel()
    }


    return render(request, 'AppTravel/reserva_hotel.html',contexto)


@login_required
def busqueda(request):
    busqueda = request.GET.get('buscar')
    hotel=""
    hoteles = Hotel.objects.filter(user = request.user)
    vuelos = Vuelo.objects.filter(user = request.user)
    vuelo = ""

    if busqueda:
        
        hotel = Hotel.objects.filter(nombreH__nombreh__icontains=busqueda).filter(user = request.user)
        
        if busqueda:

            vuelo = Vuelo.objects.filter(destino__destino__icontains=busqueda).filter(user = request.user)
        

    else:
        messages.info(request,"No se pudo buscar, intente con otra palabra")
           


    contexto = {
        'hoteles':hoteles,
        'vuelos':vuelos,
        'hotel':hotel,
        'vuelo':vuelo


    }

    return render(request, 'AppTravel/busqueda.html',contexto)


def about(request):

    return render(request, 'AppTravel/about.html')








